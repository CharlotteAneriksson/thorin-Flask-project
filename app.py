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

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member )

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


