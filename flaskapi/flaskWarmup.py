#!/usr/bin/python3

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from questionBank import QandA

app = Flask(__name__)
## This is where we want to redirect users to

@app.route("/") 
def start():
    print(QandA)
    return render_template("question.html")

@app.route("/correct") 
def correct():
    return render_template("correct.html")


@app.route("/answer", methods =["POST"])
def answer():
    if request.method == "POST":
        if request.form.get("ans"): 
            answer1 = request.form.get("ans") 
            if answer1 =='Louisiana':
                return redirect(url_for("correct"))
    
    return redirect(("/"))
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application