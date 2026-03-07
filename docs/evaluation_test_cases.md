5. Evaluation Starter Kit (Minimum 20 Test Cases)
Create:

/docs/evaluation_test_cases.md
Include 20 scenarios with:

Pantry snapshot (ingredients + quantities + expiry)
Expected feasibility result (Pass/Fail)
Generated recipe output
Validator output
Notes (what failed and why, if fail)
Required metrics
Feasibility pass rate
“Invented ingredient” rate (should be 0 in default mode)
Expiry utilization rate (if you claim expiry-first)
Average regeneration attempts (if using regenerate-on-fail)

> click on Images on Pantry Snapshot for better view

# Test Cases

| ID | Test Case Name | Pantry Snapshot | Expected Result | Actual Result | Status (✅/❌) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** |Not Enough Sugar |<img src="images/DB_num1.png" width="100"> |Pass |Pass: <br> <img src="images/DB_num1_Result.png" width="100"> <img src="images/DB_num1_Result2.png" width="100"> |✅ |Scaled down the recipe |
| **02** |Expired Chicken Breast |<img src="images/DB_num2.png" width="100"> |Pass |Pass: <br> <img src="images/DB_num2_Result.png" width="100"> <img src="images/DB_num2_Result2.png" width="100">|✅ |Did not generate a recipe with expired ingredient |
| **03** |Cherries Are Not in the Inventory |<img src="images/DB_num3.png" width="100"> |Pass |Pass: <br> <img src="images/DB_num3_Result.png" width="100"> |✅ |Did not generate a recipe with an item not in the inventory |
| **04** |Expired Milk |<img src="images/DB_num4.png" width="100"> |Pass |Pass: <br> <img src="images/DB_num4_Result.png" width="100"> <img src="images/DB_num4_Result2.png" width="100"> |✅ |Did not generate a recipe with expired ingredient |
| **05** |Expiry First |<img src="images/DB_num5.png" width="100"> |Pass |Pass: <br> <img src="images/DB_num5_Result.png" width="100"> <img src="images/DB_num5_Result2.png" width="100">|✅ |Recommended a recipe with expiring ingredients |
| **06** |Non-food Item |<img src="images/DB_num6.png" width="100"> |Pass |Pass: <br> <img src="images/DB_num6_Result.png" width="100"> |✅ |Did not recommend a recipe with a non-food item |
| **07** |Scaling down Multiple Items |<img src="images/DB_num7.png" width="100"> |Fail |Fail: <img src="images/DB_num7_Result.png" width="100"> <img src="images/DB_num7_Result2.png" width="100"> |❌ |Unit conversion was unsuccessful |
| **08** |2 Fresh, 1 Expired |<img src="images/DB_num8.png" width="100">  |Pass |Pass: <br> <img src="images/DB_num8_Result.png" width="100"> <img src="images/DB_num8_Result2.png" width="100"> |✅ |Did not use expired ingredient in the recipe |
| **09** |Food Safety Advice |<img src="images/DB_num9.png" width="100"> |Pass |Pass: <img src="images/DB_num9_Result.png" width="100"> |✅ |Did not offer food safety advice |
| **10** |Eggplant Fettuccine + Soap |<img src="images/DB_num10.png" width="100"> |Pass |Fail: <br> <img src="images/DB_num10_Result.png" width="100"> <img src="images/DB_num10_Result2.png" width="100">|❌ |Ignored soap but unit conversion failed |
| **11** |Pantry with a small amount of inventory| <img src="images/DBT_num11.png" width="100"> |Fail:|Fail: <img src="images/num11_results.png" width="100"> | ❌| |
| **12** | | | | | | |
| **13** | | | | | | |
| **14** | | | | | | |
| **15** | | | | | | |
| **16** | | | | | | |
| **17** | | | | | | |
| **18** | | | | | | |
| **19** | | | | | | |
| **20** | | | | | | |



