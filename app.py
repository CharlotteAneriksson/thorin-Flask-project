import json
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", 
    company = data) 
    #page_title is a serverside set variable
    """
    list_of_numbers is a list created and added in base to not repeat ourselfs
    """

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


