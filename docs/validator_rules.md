/docs/validator_rules.md (bullet list of rules)

#Validator Rules 

1. JSON must be correctly formatted. If it isn't, give: Please output strictly in the requested JSON format
2. Expired ingredients cannot be used for generating a recipe. If they are AI responds: Ingredient 'x' is expired and cannot be used.
3. The LLM response must be generated with the existing ingredient from the user DB. If it doesn't: Ingredient 'x' is not in the pantry.
4. The LLM must not exceed the current user's ingredient Quantity. If there's not enough, then: Not enough 'x'. Need 'x'ml, but only have 'x'ml available. Please scale down portions/servings.
5. The units must be converted.
   
