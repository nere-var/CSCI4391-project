from flask import Flask, render_template, request
import json
import urllib.request
from urllib.parse import quote_plus

#inpired by 
# https://youtu.be/69IJoRo4ax0?si=cvigd-RJdW-DcKZd
 

app = Flask(__name__)

# -------------------- Home Page --------------------
@app.route("/")
def home_page():
    return render_template("HomePage.html")

# -------------------- Other Page can go here --------------------

# -------------------- Run App --------------------
if __name__ == '__main__':
    app.run(debug=True)
    
    
    