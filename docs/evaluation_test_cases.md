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
| **11** |Small DB with a lot of expired inventory 
| <img src="images/DB_num11.png" width="100"> |Fail:|Fail: <img src="images/num_11_result.png" width="100"> | ✅| Did not generate recipe with items that were not in the inventory   |
| **12** |Trying to generate recipe with expired inventory
 | <img src="images/DB_num12.png" width="100"> | Fail: | Fail: <img src="images/number_12_result1" width="100">  <img src="images/number_12_result2" width="100"> | ✅ | Did not generate with expired inventory|
| **13** |Big DB generation with 5 expired inventory|<img src="images/DB_num13.png" width="100"> |Pass: |Pass:  <img src="images/number_13_result1" width="100">  <img src="images/number_13_result2" width="100"> | | |
| **14** |Fairly big  DB with no expired inventory 
 |<img src="images/DB_num14.png" width="100"> | Pass |??: <img src="images/number_14_result1" width="100">  <img src="images/number_14_result2" width="100"> | | |
| **15** |DB with 27 expired and one fresh inventory
 |<img src="images/DB_number_15.png" width="100"> |Fail |:  <img src="images/number_15_result1" width="100">  <img src="images/number_15_result2" width="100"> | | |
| **16** |DB with only meat and trying to get a vegan meal
 |<img src="images/DB_number_16.png" width="100"> |Fail |: <img src="images/number_16_result1" width="100">  <img src="images/number_16_result2" width="100"> | | |
| **17** |DB with only items to make something sweet
 |<img src="images/DB_number_17.png" width="100"> |Pass: |:  <img src="images/number_17_result1" width="100">  <img src="images/number_17_result2" width="100"> | | |
| **18** |DB with only vegan options 
|<img src="images/DB_number_18.png" width="100">  | Pass: |: <img src="images/number_18_result1" width="100">  <img src="images/number_18_result2" width="100">  | | |
| **19** |DB with incorrect inventory |<img src="images/DB_number_19.png" width="100">  |Fail: |:<img src="images/number_19_result1" width="100">  | | |
| **20** |DB suitable for making a variety of Asian cuisine recipes |<img src="images/DB_number20.png" width="100"> |Pass: |:<img src="images/number_20_result1" width="100">  <img src="images/number_20_result2" width="100"> <img src="images/number_20_result3" width="100">  | | |



