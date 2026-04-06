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


| ID | Starting State | Login credentials used for demo | Pantry state used in happy path | Prompt used in happy path | expected validator pass behavior | pantry state used in failure path | expected validator fail/refusal behaviour |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ID | Login | empty:empty | empty | I want a recipe for fries | no potatoes in inventory displayed | empty pantry | gives recipe for fries |
| ID | Login | demo:demo | full | I want a recipe with chicken breast in it please | validator should tell you that the chicken in the inventory is expired | full | the recipe is generated without even a warning of expired items |
| ID | Login | demo:demo | full | I would like a recipe for chicken stew | inventory check for chicken, finds chicken breast that is expired and replaces with chicken thigh or chicken wing | only expired chicken | expired chicken used |

