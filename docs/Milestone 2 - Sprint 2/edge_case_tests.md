# Edge Test Cases
Test with: empty pantry, all items expired, single ingredient, conflicting dietary restrictions

| ID | Test Case Name | Pantry State | User Prompt | Expected Result | Actual Result | Status (✅/❌) | Notes | Image |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Empty Pantry |  |  | The user will recieve a response saying there are no ingredients in the pantry and recommend that the user adds some to get started. |  |  |  | |
| **02** | All ingredients are expired |  |  | No recipe will be generated and the user will be told that the ingredients are expired and cannot be used. |  |  |  | |
| **03** | Single ingredient in the pantry |  |  | The user will recieve a response saying there is not enough ingredients to make a meal OR a simple 1 ingredient meal will be generated. |  |  |  | |
| **04** | Conflicting dietary restrictions |  |  | AI will detect the conflict OR no recipe will be generated with an explanation. |  |  |  | |
