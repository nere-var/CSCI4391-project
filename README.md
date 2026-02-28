Document Links: [install](#install) / [usage](#usage) / [demo](#demo)
<img width="1648" height="349" alt="a" src="https://github.com/user-attachments/assets/7f49a123-4529-4f44-947b-519a546626eb" />

# Binny and Bloom
## A live well app focused on minimizing waste while maximizing utility.<center> <br />
Senior Project - Spring 2026.

<br /><br />


<br /><br />



<a name="install"></a>Installation:<br />

```
SeniorProject/
|  |
|  ├- /docs/
|  |    ├- Binny And Bloom.pdf
|  |    ├- Milestone 1 Deliverables.md
|  |    ├- PRD.md
|  |    ├- SpikePlan.md
|  |    ├- architecture.png
|  |    ├- evaluation_test_cases.md
|  |    ├- generation_strategy.md
|  |    ├- pantry_schema.md
|  |    └- validator_rules.md
|  └- /src/
|     |  |
|     |  ├- /instance/
|     |  |      ├- 01-build-db-new.py
|     |  |      ├- 02-insert-db-new.py
|     |  |      ├- 03-test-db-new.py
|     |  |      └- inventory.db
|     |  └- /static/
|     |      ├- /css/
|     |      |   ├- homestyle.css
|     |      |   └- mainstyle.css
|     |      ├- /js/
|     |      |   └- MainPageJS.js
|     |      ├- /Pictures/
|     |      |   ├- Binny-original.png
|     |      |   ├- Binny.png
|     |      |   ├- chef.png
|     |      |   ├- favicon.png
|     |      |   └- trail.png
|     |      └- /profile_pics/
|     |          └- demo.png
|     ├- /templates/
|     |    ├- 0-AIPageSetup.html
|     |    ├- 0-AddItemPageSetup.html
|     |    ├- 0-HomePageSetup.html
|     |    ├- 0-InventoryPageSetup.html
|     |    ├- 0-MainPageSetup.html
|     |    ├- 0-SamplePageSetup.html
|     |    ├- AddItemPage.html
|     |    ├- HomePage.html
|     |    ├- InventoryPage.html
|     |    ├- LoginPage.html
|     |    ├- RegisterPage.html
|     |    ├- SamplePage.html
|     |    ├- ScoreboardPage.html
|     |    ├- UserProfile.html
|     |    └- dashboard.html
|     ├- .env
|     ├- app.py
|     ├- database.py
|     ├- generator.py
|     ├- models.py
|     ├- openrouterllm.py
|     ├- requirements.txt
|     ├- unit_conversion.py
|     └- validatory.py
├- .gitignore
├- README.md
└- requirements.txt
 ```





<br /><br />
To install necessary packages after pulling repo:
- ```python -m venv .venv```        # create virtual environment
- ```.venv\Scripts\activate```      # activate it
- ```pip install -r requirements.txt```   # installs all packages listed

For Mac/Linux Users:
- ```python -m venv venv```        # create virtual environment
- ```source venv/bin/activate```      # activate it
- ```pip install -r requirements.txt```   # installs all packages listed

Then Run  
- ```python3 src/app.py```  #In the Projects root Folder
- This will start an instance of Flask which will provide GUI accessed by navigating to the address provided in a browser window:
  <img width="953" height="164" alt="image" src="https://github.com/user-attachments/assets/a4c16929-a3cb-4841-bf0b-2ff8910a1e85" />
 

<br /><br />
<a name="usage"></a>Usage:<br />

We have provided a database with a various items with username:password  demo:demo<br>
<img width="157" height="100" alt="Screenshot 2026-02-27 165230" src="https://github.com/user-attachments/assets/3265c059-7ea6-4848-af09-8919711ae2bf" /><img width="157" height="100" alt="Screenshot 2026-02-27 165411" src="https://github.com/user-attachments/assets/fbce4279-516d-482f-9f95-23bac15343dc" /><img width="157" height="100" alt="Screenshot 2026-02-27 165530" src="https://github.com/user-attachments/assets/e71e0f65-9e7e-4cdb-b49f-e1dba067b101" /><img width="157" height="100" alt="Screenshot 2026-02-27 165500" src="https://github.com/user-attachments/assets/13f25fb5-2719-4a2e-880f-064adb6ec2a0" /><br>
The inventory page shows all of the items the current user has available in their inventory and just below that is field to interact with the AI:<br>
<img width="157" height="100" alt="Screenshot 2026-02-27 165611" src="https://github.com/user-attachments/assets/dfcccf90-bc63-4d67-9940-6b452cc2f599" /><img width="157" height="100" alt="Screenshot 2026-02-27 165638" src="https://github.com/user-attachments/assets/d8083efb-3581-406e-a217-6c4f27c19bd0" /><img width="157" height="100" alt="Screenshot 2026-02-27 165707" src="https://github.com/user-attachments/assets/d41f3094-4cae-44db-922a-a65057086a04" />
<br>
If Binny finds a recipe that can be made with only item available in the user's inventory:<br>
<img width="157" height="100" alt="Screenshot 2026-02-27 170105" src="https://github.com/user-attachments/assets/109e1e78-2f98-4231-9cf1-b0aecb2e4b2c" /><br>
If the ingredients are not available:<br>
<img width="157" height="100" alt="Screenshot 2026-02-27 165840" src="https://github.com/user-attachments/assets/83fda730-90af-400d-b462-a667191799bd" />













<br /><br /><br />


<br /><br /><br />

<a name="demo"></a>Demo:<br />

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Hfm94aHAbYQ/0.jpg)](https://www.youtube.com)



<br /><br /><br /><br />

The Krusty Compost Crew<br />
<a href="https://github.com/picklefarm1234" title="Abigail R"><img width="50" height="50" alt="profile image" src="https://avatars.githubusercontent.com/u/230457100?v=4" /></a>
<a href="https://github.com/AlexandriaTH" title="Taja H"><img width="50" height="50" alt="profile image" src="https://avatars.githubusercontent.com/u/118304167?v=4" /></a>
<a href="https://github.com/OrangeXR" title="Luis M"><img width="50" height="50" alt="profile image" src="https://avatars.githubusercontent.com/u/77978673?s=64&v=4" /></a>
<a href="https://github.com/jayv2025" title="Jay V"><img width="50" height="50" alt="profile image" src="https://avatars.githubusercontent.com/u/179060597?v=4" /></a>
<a href="https://github.com/nere-var" title="Emma "><img width="50" height="50" alt="profile image" src="https://avatars.githubusercontent.com/u/58350011?v=4" /></a>

