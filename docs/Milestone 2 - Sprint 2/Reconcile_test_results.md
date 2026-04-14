# MVP test cases (10, all passing) contradict evaluation results (6/20 failing). Reconcile and produce honest, consistent results


# click on Images on Pantry Snapshot for better view

| ID | Test Case Name | Pantry state | User prompt | expected result | actual result | Status (✅/❌) | Notes 
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | CLI1 - Asking for recipe with non inventory item |  | Can you make me a recipe with chicken please? | LLM should not generate recipe since ingredient isnt available in the pantry |  | ✅| The LLM Did not generate recipe, and even recomds to generate with a inventory item the user does have  |
| **02** | CLI2 - Asking for recipe on a fairly large DB |  | Can you make me a simple but tasty recipe please?| Should generate recipe with correct measurement types |  | ❌ | The LLM did generate a recipe, but it does not give any measurement types in the cooking instructions. |
| **03** | CLI3 - Asking for recipe on all expired DB  |  | Can you make me a tacos recipe please? | LLM should not generate recipe since ingredient are all expired in the pantry  |  |✅ | The LLM Did not generate recipe, since ingredients were expired |
| **04** | CLI4 - Asking for a recipe on a small inventory |  | Make me a recipe that uses bagels  | Should not generate something or generate something only using the invenotry we have |  |✅ | The LLM Did not generate recipe since it doesnt have enough ingredients |
| **05** | CLI5 - Asking for a recipe using an item you cant eat |  | Hi can you make me a recipe using poop please?  | Should not generate anything |  | (✅/❌) | The LLM gave the correct expected response |
| **06** | CLI6 - |  |  |  |  | |  |
| **07** | CLI7 - |  |  |  |  | |  |
| **08** | CLI8 - |  |  |  |  | |  |
| **09** | CLI9 - |  |  |  |  | |  |
| **10** | CLI10 - |  |  |  |  | |  |
| **11** | FLASK1 - |  |  |  |  | |  |
| **12** | FLASK2 - |  |  |  |  | |  |
| **13** | FLASK3 - |  |  |  |  | |  |
| **14** | FLASK4 - |  |  |  |  | |  |
| **15** | FLASK5 - |  |  |  |  | |  |
| **16** | FLASK6 - |  |  |  |  | |  |
| **17** | FLASK7 - |  |  |  |  | |  |
| **18** | FLASK8 - |  |  |  |  | |  |
| **19** | FLASK9 - |  |  |  |  | |  |
| **20** | FLASK10 - |  |  |  |  | |  |

