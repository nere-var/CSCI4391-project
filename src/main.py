import sqlite3
import datetime
from openrouterllm import Ai_Chat
from werkzeug.security import check_password_hash
from validator import recipe_validator
import json

# ==================
# open db connection
# ==================
def get_db():
    conn = sqlite3.connect("src/Instance/Inventory.db")
    conn.row_factory = sqlite3.Row
    return conn
    


# ==================
# choose user
# ==================
# =========================================================================== no password login
#def choose_player():                                                       # 
#    db = get_db()                                                          # 
#    players = db.execute("SELECT id, name FROM players").fetchall()        #    
#    db.close()                                                             #   
#                                                                           #      
#    print("\nAvailable Players:")                                          #  
#    for p in players:                                                      #      
#        print(f"{p['id']}: {p['name']}")                                   #              
#                                                                           #          
#    return int(input("\nEnter player ID: "))                               #      
# ============================================================================ no password login
# ============================================================================ password required
def choose_player():                                                                           #
    db = get_db()                                                                              #
    players = db.execute("SELECT id, name FROM players").fetchall()                            #
    db.close()                                                                                 #
                                                                                               #
    print("\nAvailable Players:")                                                              #
    for p in players:                                                                          #
        print(f"{p['id']}: {p['name']}")                                                       #
                                                                                               #
    player_id = int(input("\nEnter player ID: "))                                              #
                                                                                               #
    # Fetch stored password hash                                                               #
    stored_hash = get_player_password_hash(player_id)                                          #
                                                                                               #
    if stored_hash is None:                                                                    #
        print("Invalid player ID.")                                                            #
        return choose_player()                                                                 #
                                                                                               #
    # Ask for password until correct                                                           #
    while True:                                                                                #
        password = input("Enter password: ").strip()                                           #
                                                                                               #
        if check_password_hash(stored_hash, password):                                         #
            print("Login successful!\n")                                                       #
            return player_id                                                                   #
        else:                                                                                  #
            print("Incorrect password. Try again.\n")                                          #
# ============================================================================ password required




# ======================================                         
# Validate Login(get hash from database)                         
# ======================================                           
# ================================================================ #
def get_player_password_hash(player_id):                           #
    db = get_db()                                                  #
    row = db.execute(                                              #
        "SELECT password_hash FROM players WHERE id = ?",          #
        (player_id,)                                               #
    ).fetchone()                                                   #
    db.close()                                                     #
    return row["password_hash"] if row else None                   #
# ================================================================ #






# =====================
# get inventory
# =====================
def get_inventory(player_id):
    db = get_db()
    items = db.execute(
        "SELECT * FROM inventory WHERE player_id = ? AND status = 'active'",
        (player_id,)
    ).fetchall()
    db.close()
    return (items)



# =====================
# get items by date
# =====================
def get_inventory_by_date(player_id):
    db = get_db()
    items = db.execute(
        """
        SELECT name, quantity, unit, best_by
        FROM inventory
        WHERE player_id = ? AND status = 'active'
        ORDER BY best_by ASC
        """,
        (player_id,)
    ).fetchall()
    db.close()

    print("\n=== Foods and Best-By Dates ===")
    if not items:
        print("No active inventory items found.")
        return

    for item in items:
        name = item["name"]
        qty = item["quantity"]
        unit = item["unit"]
        best_by = item["best_by"] if item["best_by"] else "No date"

        print(f"- {name} ({qty} {unit}) — Best by: {best_by}")



# =====================
# add item to inventory
# =====================
def add_item(player_id):
    print("\n=== Add New Inventory Item ===")

    # Basic fields
    name = input("Item name: ").strip()
    category = input("Category (meat, seafood, dairy, produce, grains, pantry, frozen, snack, beverages): ").strip()
    quantity = float(input("Quantity: "))
    unit = input("Unit (g, kg, lb, oz, ml, fl_oz, cup, tbsp, tsp, liter, gallon, half_gallon, each): ").strip()
    measurement_type = input("Measurement type (weight, volume, count): ").strip()

    # Optional normalized quantities
    q_grams = input("Quantity in grams (optional): ").strip()
    quantity_grams = float(q_grams) if q_grams else None

    q_ml = input("Quantity in ml (optional): ").strip()
    quantity_ml = float(q_ml) if q_ml else None

    # Dates
    purchase_date = input("Purchase date (YYYY-MM-DD): ").strip()
    best_by = input("Best-by date (YYYY-MM-DD): ").strip()

    # Boolean flags
    raw_meat = 1 if input("Raw meat? (y/n): ").lower() == "y" else 0
    perishable = 1 if input("Perishable? (y/n): ").lower() == "y" else 0
    opened = 1 if input("Opened? (y/n): ").lower() == "y" else 0
    donation_allowed = 1 if input("Donation allowed? (y/n): ").lower() == "y" else 0
    decomposition_flag = 1 if input("Decomposition flag? (y/n): ").lower() == "y" else 0

    # Price
    price = float(input("Price per item: "))

    # Force status to active
    status = "active"

    # Insert into DB
    db = get_db()
    db.execute(
        """
        INSERT INTO inventory (
            player_id, name, category, quantity, unit, measurement_type,
            quantity_grams, quantity_ml, purchase_date, best_by,
            raw_meat, perishable, opened, donation_allowed, decomposition_flag,
            price, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            player_id, name, category, quantity, unit, measurement_type,
            quantity_grams, quantity_ml, purchase_date, best_by,
            raw_meat, perishable, opened, donation_allowed, decomposition_flag,
            price, status
        )
    )
    db.commit()
    db.close()

    print("\nItem added successfully!")





# =====================
# generate Binny Menu
# =====================
def binny_menu(player_id):
    chat = Ai_Chat() # Ai_Chat() handles keys (and most of the heavy lifting)
    # pull latest db items every turn 
    inventory_items = chat.get_active_inventory(player_id)
    inventory_context = chat.build_inventory_context(inventory_items)

    user_message = input("\nAsk Chef Binny something: ")
    # append user message to conversation
    messages = [
        {
            "role": "system",
            "content": (
                 "You are a helpful, eco-conscious cooking assistant.\n"
                 "Only use the inventory provided to you.\n"
                 "When suggesting recipes or meals:\n"
                 "- Be specific and precise with ingredient quantities.\n"
                 "- Use realistic measurements (grams, ml, tbsp, cups, etc.).\n"
                 "- Respect the available inventory amounts.\n"
                 "- Do not suggest quantities that exceed what is available.\n"
                 "- If quantity data is missing, state assumptions clearly.\n"
                 "Keep responses concise but practical and clear."
                 "Do not give food safety recommendations at all. Anything involving food safety, respond 'Sorry, I don't have that info.'\n"
                 "Format all responses as clean plain text. Avoid tables, table-like structures, columns, or spreadsheet-style formatting. Use paragraphs or bullet points instead.")
        },
        {
            "role": "system", "content": f"Current Inventory:\n{inventory_context}"
        },
        {
            "role": "user", "content": user_message
        }
    ]

#    response = chat.getLLMResponse(messages)
#
#
#    # ===============================================================
#    recipe = {
#        "response": response,
#        "player_Id": player_id
#    }
#    chat.save_result_JSON(recipe)  # saves to saved_recipe.json by default
#
#    validator_instance = recipe_validator()
#    validator_instance.read_from_JSON("saved_recipe.json")
#    # ================================================================






#    print("\n=== BinnyBot Response ===\n")
#    print(response)








    response = chat.getLLMResponse(messages)

    # Validate using your validator
    validator_instance = recipe_validator()
    is_valid, validation_msg = validator_instance.validate_AI_recipe(response, player_id)

    print("\n=== BinnyBot Response ===\n")
    print(response)

    print("\n=== Validation ===\n")
    print(validation_msg)
















    


# ========================================================================================================================================
# ========================================================================================================================================
# main
# ========================================================================================================================================
# ========================================================================================================================================

def main():
    # ===========
    # Select User
    # ===========
    print("\n=== Binny Recipe Generator ===")
    player_id = choose_player()


    # =========
    # Main Menu
    # =========
    while True:
        print("\nOptions:")
        print("1. View Inventory")
        print("2. View Foods + Best-By Dates")
        #print("3. Add Item to Inventory")
        print("4. Generate Binny Recipe")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            items = get_inventory(player_id)
            print("\nInventory:")
            for item in items:
                print(f"- {item['name']} ({item['quantity']} {item['unit']})")

        elif choice == "2":
            get_inventory_by_date(player_id)
            
        #elif choice == "3":
        #    add_item(player_id)

        elif choice == "4":
            binny_menu(player_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()