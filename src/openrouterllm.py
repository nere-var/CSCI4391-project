import requests
import os
import sqlite3
from dotenv import load_dotenv

# IMPORTANT
# I sent the .env file with the api key  in the chat, but I will not be including it in the code repository for security reasons and github gets whiny about it lol
# Just drop that .env file in the same directory as this script and it should work fine
# I have that .env file added to .gitignore so it wont be included in the repo
# thanks guys :3

load_dotenv() # load environment variables from .env file

# set api key and endpoint 
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please check your .env file and ensure OPENROUTER_API_KEY is set.")
API_URL = 'https://openrouter.ai/api/v1/chat/completions' # api url, program will send requests and get responses from here

# restricted words/topics, chatbot will not responsd
RESTRICTED_WORDS = ["poop"]

# db path + other variables
DB_PATH = 'src/instance/inventory.db'
PLAYER_ID = 1 # for testing
MAX_HISTORY = 10 # max number of messages to keep in conversation history to prevent growth

# DB setup
def get_db(): # function to connect to the database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_active_inventory(player_id): # function to get active inventory items for a player from the database
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(""" 
        SELECT name, category, quantity, unit,
               quantity_grams, quantity_ml,
               best_by, opened
        FROM inventory
        WHERE player_id = ? AND status = 'active'
    """, (player_id,)) # fetch all active inventory items for the player, including quantity in grams and ml for better precision in recipe suggestions

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows] # return list of dicts representing inventory items, each dict has keys: name, category, quantity, unit, quantity_grams, quantity_ml, best_by, opened

def build_inventory_context(items):
    if not items:
        return "No food items in inventory."
    # build a string representation of the inventory items to provide context to the LLM, including quantity and best by date
    lines = [] 
    for item in items:
        qty = f"{item['quantity']} {item['unit']}" if item['quantity'] else "Unknown qty"

        line = (
            f"{item['name']} | "
            f"{qty} | "
            f"Best by: {item['best_by']} | "
            f"Opened: {bool(item['opened'])}"
        )
        lines.append(line)

    return "\n".join(lines)

# get llm response functions
def getLLMResponse(messages):
    # set headers and data for the request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openrouter/free",  # free models router
        "messages": messages # will declare limits at start of chat loop
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status() # check for errors
        responseData = response.json()

        return responseData['choices'][0]['message']['content'] # return the content of the response
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        return f"Error: {e}"
    
# console chat loop

def chatConsole():
    print("Welcome! this is a test run of using openrouter free. type 'quit' to exit.\n")

    # this is where the chatbot will be constrained
    messages = [
            { "role": "system", 
                "content": (
                            "You are a helpful, eco-conscious cooking assistant.\n"
                            "Only use the inventory provided to you.\n"
                            "When suggesting recipes or meals:\n"
                            "- Be specific and precise with ingredient quantities.\n"
                            "- Use realistic measurements (grams, ml, tbsp, cups, etc.).\n"
                            "- Respect the available inventory amounts.\n"
                            "- Do not suggest quantities that exceed what is available.\n"
                            "- If quantity data is missing, state assumptions clearly.\n"
                            "Keep responses concise but practical and clear." )
                            }]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        #  check for forbidden words/topics
        if any(word in user_input.lower() for word in RESTRICTED_WORDS):
            print("LLM: Sorry, I can't discuss that topic.\n")
            continue

        # pull latest db items every turn 
        inventory_items = get_active_inventory(PLAYER_ID)
        inventory_context = build_inventory_context(inventory_items)

        # append user message to conversation
        messages.append({"role": "system",
                         "content": f"Current Inventory:\n{inventory_context}" # provide current inventory context to the LLM every turn so it can make informed suggestions based on what the player has available
        })

        messages.append({"role": "user", "content": user_input}) 
        
        # limit conversation history to last 10 messages to stay within token limits
        messages[:] = messages[-MAX_HISTORY:]

        response = getLLMResponse(messages) 

        print(f"LLM: {response}\n") # 

        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    chatConsole()    