#todo: add code for saving win/loss record using json and/or database
#add more gui elements using css/javascript
#make the computer AI more intelligent when making a selection
#incorporate database by creating log in page.
#create a "log in" page as part of home
from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename
from random import randrange
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('rps',__name__)
empty = True #created this so that the page knows if someone has made a selection between rock, paper, or scissors yet. 
logged_in= False #by default the home page will know that the user is not logged in
@bp.route('/')
def home(): #should be the first page the users sees. The variable new is set to True and that's what home.html will use to choose what it will show the user
   return render_template('home.html', codes=session.keys(), new=empty)
#investigate reload function for home page with if statement for if something selected or not that way, you do everything in one html page.
@bp.route('/', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST': #this should come up after the user makes a selection of rock, paper, or scissor
        empty=False #changed variable to False so that the page loads the correct part of home.html
        choice_dict = {0: 'Rock', 1: 'Paper', 2: 'Scissors'} #mapping numbers to the possible choises.
        cpu_chose = choice_dict[randrange(3)] #using a random selector, the computer will chose either rock, paper or scissors. The interger will act as a key to the map and the variable will save the value.
        return render_template('home.html',  selection = request.form['selection'],new = empty, cpu_select = cpu_chose)

    else:
        pass # unknown
 
