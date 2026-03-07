# Choose one: Option A: Two-stage plan (recommended) (picked)

    Deterministic planner selects a feasible ingredient subset + target dish type
    LLM writes the recipe using only the selected subset + exact amounts

Create:
    
    /docs/generation_strategy.md (which option you used and why)
    we decided to use this becuase ......



============================================================================================


    
# Option C: Constraint-guided decoding (lightweight)
### Use structured JSON output format from LLM
### Reject outputs failing schema/constraints and regenerate
<br><br>
Our project uses a two‑stage generation workflow to ensure that all AI‑generated recipes are:
Realistic using only the user's actual inventory
Accurate(no inventing ingredients, realistic amounts, correct units)
Deterministic planner but creative dishes

This approach prevents hallucinating ingredients, the ignoring of quantities, or producing vague instructions.
<br><br>
Why option A was chosen
Option A was selected because it gives the best balance of control, creativity, and reliability.  These are especially important for our app since:
Recipes must use only items from the user's inventory
Filters out expired items
Selects a subset of ingredients
Chooses a type of dish
Suggests exact quantities for each ingredient
Creates a structured JSON plan:
```
<<     JSON STRUCTURE WOULD GO HERE.     >>
```

and then more text down here



