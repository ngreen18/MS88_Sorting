# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import Flask
from flask import render_template
from flask import request
from model import compare
from model import house_selector

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/results", methods = ["POST", "GET"])
def results():
    if request.method == "POST":
        print(list(request.form.listvalues()))
        answers = list(request.form.listvalues())
        compare(answers)
        school_house = house_selector()
        return render_template('results.html', school_house = school_house)
    else:
        return "Error"
