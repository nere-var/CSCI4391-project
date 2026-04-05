# MVP Retrospective 

In 1 to 2 pages, explain:
- what changed from Milestone 1 to Milestone 2
- what was cut from scope
- what is now truly MVP-ready
- what still needs work after MVP


# What changed from Milestone 1 to Milestone 2
- There have been several changes and improvements to our development of Binny and Bloom recently. The first notable change is that we have implemented better
  ingredient matching. This avoids the issue of the validator not correctly matching ingredients even though they are available in the pantry. In cases such as:
  * "chicken breast" vs "chicken"
  * plural/singular differences
    
- The normalizeIngredient(name): does lowercase and trim whitespaces
  * egg vs eggs
    
- The ingredients_match(req_name, inv_name) handles the ingredients matching
  * chicken thighs and chicken breast → both count as "chicken."
  * milk vs whole milk
  * Ground beef → counts as turkey

- Another change we made was to implement our LLM into our Flask website.
  We made sure to add a small chatbot pop-up that lets the user chat and ask the BinnyBot  to create and suggest recipes.This returns the appropriate validation
  message.   

# What was cut from scope




# What is now truly MVP-ready




# What still needs work after MVP

- The implementation of decomposing and donations still needs to be included. Another necessary thing we still need to add is a function that decreases the amount of the pantry once the user decides to use a recipe or decompose, etc. In the front end, we still need to continue improving our UI. Improvements towards the LLM still need to be done.

NOT DONE - Due 4-5-26
