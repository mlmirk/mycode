#!/usr/bin/python3

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from random import randint




QandA = {
    0:
    {
    "Question": "When is Harry Potter's birthday?",
    1:"July 1st", 
    2:"May 31st",
    3:"July 31st" ,
    4:"October 7th",
    "A":3} , 
    1:
    {
    "Question": "What is the first thing Romilda Vane offers Harry that is spiked with a love potion?",
    1:"Cauldron Cakes", 
    2:"Fizzing Whizbees",
    3:"Firewhisky" ,
    4:"Gillywater",
    "A":4} , 
    2:
    {
    "Question": "What is the first password into the Gryffindor commonroom?",
    1:"Caput Draconis", 
    2:"Fortuna Major",
    3:"Baubles" ,
    4:"Pig Snout",
    "A":1} , 
    3:
    {
    "Question": "How many staircases are in Hogwarts?",
    1:"364", 
    2:'142',
    3:"994" ,
    4:"993",
    "A":2} , 
    4:
    {
    "Question": "Besides peace between Wizard's and Muggles, what would Gilderoy Lockhart not mind having for a birthday present?",
    1:"The sixth nomination for Witch Weekly's most charming smile award.", 
    2:"A bottle of Odgen's Old Firewhisky",
    3:"A signed record from Christina Warbeck" ,
    4:"A large box of Fizzing Wizbees",
    "A":2} , 
    5:
    {
    "Question": "When do you first hear of the Room of Requirement, and who was the user?",
    1:"Order of the Phoenix and Dobby", 
    2:"Goblet of Fire and Dumbledore",
    3:"Order of the Phoenix and the DA" ,
    4:"The Prisoner of Azkaban and Remus Lupin",
    "A":2} , 
    6:
    {
    "Question": "Why did Cormac McLaggen miss the Quidditch tryouts in the year previous to Harry Potter and the Half-Blood Prince?",
    1:"He grew an extra leg due to a dueling accident.t", 
    2:"He was in detention for melting his cauldron in potions class.",
    3:"He broke his knee when he fell through a trick step." ,
    4:"He ate a pound of doxy eggs for a bet.",
    "A":4} , 
    7:
    {
    "Question": "What is the name of the Quidditch move where a seeker fake's seeing the snitch and dives to the ground but pulls out of the dive just in time, but the opposing seeker plummets to the ground?",
    1:"Wonky Fent", 
    2:"Wonky Faint",
    3:"Wronsky Feint" ,
    4:"Wronsky Faint",
    "A":3} , 
    8:
    {
    "Question": "Who teased Moaning Myrtle about her glasses that lead to Myrtle crying in the washroom before getting killed?",
    1:"Marrieta Edgecomb", 
    2:"Olive Hornby",
    3:"Marcus Long" ,
    4:"Jonathan Prewet",
    "A":2} , 
    9:
    {
    "Question": "What was Lupin's code name on the radio show 'Potter Watch?'",
    1:"Romulus", 
    2:'River',
    3:"Rapier" ,
    4:"Rabies",
    "A":1} , 
    10:
    {
    "Question": "What is Luna's Patronus?",
    1:"An otter", 
    2:'A lynx',
    3:"A horse" ,
    4:"A rabbit",
    "A":4} , 
    11:
    {
    "Question": "What are the names of Severus Snape's parents?",
    1:"Toby Snape and Elly Priest", 
    2:'Tobias Snape and Ellen Prince',
    3:"Tobias Snape And Eileen Prince" ,
    4:"Tony Snape and Eileen Prince",
    "A":3}
    
}



x=0
correct=0
def main():
    app = Flask(__name__)
    @app.route("/",methods =["GET","POST"]) 
    def start():
        global x,correct
        while x < QandA.__len__():
            if request.method == "GET":
                return render_template("newquestion.html", question= QandA[x] , incorrectCorrect = False, correctAns=correct )
            if request.method == "POST":
                if request.form.get("ans"): 
                    answer1 = request.form.get("ans") 
                    if int(answer1) == QandA[x]["A"]:
                        correct+=1
                        x+=1
                        return redirect(("/"))
                else:
                    x+=1
                    return render_template("newquestion.html",question= QandA[x], incorrectCorrect = True ,correctAns=correct)
            return render_template("Final.html",correctAns=correct)


    app.run(host="0.0.0.0", port=2224) # runs the application
    
    
    
    
    """
    @app.route("/correct") 
    def correct():
        newNum()
        return render_template("newquestion.html",question= QandA[questNum],incorrectCorrect = False)
    
    @app.route("/answer", methods =["POST"])
    def answer():
        print(request.form.get("ans")) 
        if request.method == "POST":
            if request.form.get("ans"): 
                answer1 = request.form.get("ans") 
                if int(answer1) == QandA[questNum]["A"]:
                    return redirect(url_for("correct"))
        temp=False
        return render_template("newquestion.html",question= QandA[questNum], incorrectCorrect = True)
        """
    
    
if __name__ == "__main__":
    main()