# Runbook for Binny & Bloom
## 1. Prerequisites
System Requirements
- Python 3.10+
- pip
- SQLite3 installed on system
- Internet access (AI model calls)
- Git (optional but recommended)

Required Python Packages
Installed via requirements.txt:
- Flask
- python-dotenv
- sqlite3

## 2. Environment Setup
Clone the Repository
- ```git clone https://github.com/nere-var/CSCI4391-project```
- ```cd inventory-ai-recipe-generator```
2.2 Create Virtual Environment
- ```python -m venv venv```
- ```source venv/bin/activate```   # macOS/Linux
- ```venv\Scripts\activate```      # Windows
2.3 Install Dependencies
- ```pip install -r requirements.txt```



## 3. Environment Variables (.env)

- .env.example
  - ```AI_API_KEY=your_api_key_here``` 
- Create Your .env
```cp .env.example .env```
- Fill in your actual API key.



## 4. Database Setup
This project uses two new scripts to build and seed the database.

### Build the Database Schema
- ```python 01-build-db-new.py```
  - This script: Creates users, inventory, recipes, scoreboard, and any other required tables. It ensures schema consistency for all demo accounts.

### Insert Demo Data
- ```python 02-insert-db-new.py```
  - This script: Inserts demo users, seeds inventory for each demo account, inserts expired items for testing, inserts vegetarian‑only inventory for testing, seeds scoreboard entries if required



## 5. Demo Accounts
### This application includes four prebuilt demo accounts for testing:
| Username |	Password	| Description |
|---|---|---|
| demo | demo | Full pantry with normal items |
| empty | empty | No inventory items |
| expired | expired | All items expired (tests validator behavior) |
| vegetarian | vegetarian | Pantry contains only vegetarian items |


These accounts are used for:

- App testing
- Demonstrating validator behavior
- Demonstrating AI refusal logic


## 6. Running the Flask Backend
### Start the Server
- ```python src/app.py```
### Verify Successful Startup
You should see:
- ```Running on http://127.0.0.1:5000```
Open the browser and log in using any demo account.



## 7. Application Usage Guide
This section explains how to use each page.

### Inventory Page
URL: /inventory
Features:

- A complete list of items in inventory with amounts and best by dates

- Edit items: use, compost, donate, delete

- Includes window to interact with chatbot for recipe, compost, and donation requests

Expected Behaviors:

- Items in inventory will be listing by Best By date

- Add using composting donating or deleting an item with update inventory list immediately
  - Workflow:
    - User enters a prompt
    - App sends inventory + prompt to AI
    - AI returns JSON recipe
  - Validator checks:
    - Ingredient names
    - Units
    - Quantities
    - Expiration dates
  - If valid → recipe displayed
  - If invalid → refusal message shown
    - Refusal Example:
      - “Unable to create a valid recipe. Reason: no ingredients available.”
        

### Scoreboard Page
URL: /dashboard

Features:
- User Sunstainability Status
    - Novice
    - Apprentice
    - Eco-Warrior
    - Eco-Legend
- Effeiciency & Lifetime Impact
  - Total inventory acquired cost
  - Total saved per user from inventory
  - Efficiency of inventory use
- Saved Recipes  

Useful for:

- Generalization of User inventory efficiency
- Viewing and storage of recipes for user



## 8. Common Errors & How to Fix Them
### AI Returns Invalid JSON
- Symptoms:
  - “Unable to parse AI recipe”
  - JSONDecodeError
- Fix:
  - Ensure system prompt forces strict JSON
  - Retry with simpler prompt
  - Restart Flask if stuck
