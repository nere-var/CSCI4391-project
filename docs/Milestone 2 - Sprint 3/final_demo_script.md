# Demo Script

Provide the exact sequence your team will show in class:
- starting state
- login credentials used for demo
- pantry state used in happy path
- prompt used in happy path
- expected validator pass behavior
- pantry state used in failure path
- prompt used in failure path
- expected validator fail/refusal behavior
  
This should read like a checklist for a reliable live demo.

---
### Global Setup
Before demo starts:
- Backend server is running
- database is seeded with demo users
- AI and validator services are active
- inventory system is connected
- .env file has API key present

Browser is open on the login screen 

---
## Scenario 1: Login Failure (1 minute)

| steps | actions                                 | what to say                       |
|-------|-----------------------------------------|-----------------------------------|
| 1     | Leave **Username** and **Password** fields blank| |
| 2|  Click **Login** | | |

**Expected Output:**
- Login rejected, "Fill out field" message visible on the form
- User remains on login screen

**Requirements Verified:**
- System must *NOT* log the user in
- System must *NOT* load inventory or expose AI features.

---
