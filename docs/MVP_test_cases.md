# MVP Test Cases 

Provide at least 10 focused MVP test cases that directly exercise the integrated product path.
For each case include:
- test name
- pantry state
- user prompt
- expected result
- actual result
- pass/fail
- notes
  
These should be smaller and more MVP-focused than the Milestone 1 exploratory evaluation set.






> click on Images on Pantry Snapshot for better view
how you call the pic <img src="images/DB_num1.png" width="100">  just change the folder name

| ID | Test Case Name | Pantry state | User prompt | expected result | actual result | Status (✅/❌) | Notes | Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | CLI1 - Asking for recipe with empty inventory | empty | I would like a recipe for a salad | AI will reply that the inventory is empty | LLM: I tried to make a recipe, but we don't have enough ingredients. Ingredient 'tomato' is not in the pantry. | ✅ | Confirms the LLM integration correctly detects no available ingredients and produces an appropriate fallback message or empty recipe structure. | <img width="100" height="990" alt="CLI1" src="https://github.com/user-attachments/assets/580929bf-3fc6-4746-a4e1-db317a3d82f0" /> |
| **02** | CLI2 - Asking for recipe with specific item not in inventory | full | I would like a recipe for a stuffed poblano pepper | AI will reply with item not found in invetory. | FAILED: 'poblano peppers' not found in pantry. [System: Recipe failed validation: Ingredient 'poblano peppers' is not in the pantry.. Asking AI to regenerate and scale down...]|✅| Validates that the system correctly rejects recipe requests for ingredients not present in the pantry, ensuring the LLM output is validated against inventory before use, preventing invalid meal generation. | <img width="100" height="722" alt="image" src="https://github.com/user-attachments/assets/8c310744-b772-40e5-98fb-7f004f66af7d" /> |
| **03** | CLI3 - Asking for a recipe with expired ingredients | full | I would like a recipe for fries | Recipe fails because of expired item | [System: Recipe failed validation: Ingredient 'potato' is expired and cannot be used.. Asking AI to regenerate and scale down...] | ✅ | Validates that the system correctly blocks recipe generation when required ingredients are expired, ensuring the validation layer prevents unsafe or unusable items from entering recipe generation and triggers the proper regenerationor or fallback behavior. | <img width="100" height="544" alt="image" src="https://github.com/user-attachments/assets/e081b9a5-5bc7-40ba-a1b5-3db5478de05a" /> |
| **04** | CLI4 - Ask for random recipe from inventory | full | What can I cook with my inventory? | A random recipe will be generated using items from the inventory | LLM: You can make a hearty Chicken Fajita Bowl using your chicken breast, bell peppers, onion, and spices. Sauté the chicken and veggies, season with spices, and serve over rice with toppings like avocado and cheese. | ✅| Notes | <img width="598" height="816" alt="image" src="https://github.com/user-attachments/assets/01dc0cd9-c79a-4e80-b895-1e9d1d701800" /> |
| **05** | CLI5 -  | Pantry state | User prompt | expected result | actual result | Status (✅/❌) | Notes | Image |
| **06** | FLASK1 - Asking for recipe with non existing inventory | empty | I would like a recipe for fries | should return Ingredient '' is not in the pantry. | LLM: Sorry, I cannot provide a fries recipe as potatoes are not available in the inventory. | ✅ | This shows that flask correclty utilizes the Users DB  | <img width="100" height="379" alt="image" src="https://github.com/user-attachments/assets/580e69e7-1155-451a-ab35-e4a3e08a541b" /> |
| **07** | FLASK2 - Asking for recipe with expired ingredients | full | I would like a recipe for boiled spinach | AI will not recommend recipe for expired ingredients | LLM: I apologize, but I cannot provide a recipe for boiled spinach as the spinach in your inventory has expired. I'm unable to suggest recipes using expired ingredients for food safety reasons. | ✅ | The AI will validate ingredient status before recommending recipe and not recommend recipe for expired ingredients. | <img width="100" height="935" alt="image" src="https://github.com/user-attachments/assets/c23c9d7f-1df6-4942-a64c-0bbd36542307" /> |
| **08** | FLASK3 -  | Pantry state | User prompt | expected result | actual result | Status (✅/❌) | Notes | Image |
| **09** | FLASK4 -  | Pantry state | User prompt | expected result | actual result | Status (✅/❌) | Notes | Image |
| **10** | FLASK5 -  | Pantry state | User prompt | expected result | actual result | Status (✅/❌) | Notes | Image |



NOT DONE - Due 4-5-26
