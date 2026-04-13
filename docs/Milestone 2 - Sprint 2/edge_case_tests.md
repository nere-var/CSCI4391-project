# Edge Test Cases
Test with: empty pantry, all items expired, single ingredient, conflicting dietary restrictions

| ID | Test Case Name | Pantry State | User Prompt | Expected Result | Actual Result | Status (✅/❌) | Notes | Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Empty Pantry |  | "What can I make for lunch?" | The user will recieve a response saying there are no ingredients in the pantry and recommend that the user adds some to get started. | AI detects no ingredients in the user's inventory and asks them to add some to get started. | ✅ | This test case worked as expected, no ingredients were hallucinated. | |
| **02** | All ingredients are expired |  | "What can I make for dinner?" | No recipe will be generated and the user will be told that the ingredients are expired and cannot be used. | The AI did not generate any meal recommendations and explained why. | ✅ | This test case was successful, no meal was generated with the entire pantry being filled with expired ingredients. | |
| **03** | Single ingredient in the pantry |  | "What meals can I make?" | The user will recieve a response saying there is not enough ingredients to make a meal OR a simple 1 ingredient meal will be generated. |  |  |  |  |
| **04** | Conflicting dietary restrictions |  |  | AI will detect the conflict OR no recipe will be generated with an explanation. |  |  |  | |
