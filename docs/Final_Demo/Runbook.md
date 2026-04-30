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


##



##



##



##



##



##



##



##
##
##
##
