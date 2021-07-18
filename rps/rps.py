from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename
from random import randrange

bp = Blueprint('rps',__name__)
empty = True 
#todo: add code for saving win/loss record using json and/or database
#add more gui elements using css/javascript
#make the computer AI more intelligent when making a selection
@bp.route('/')
def home():
    #set something to false here. then set it to true on the post part below
   return render_template('home.html', codes=session.keys(), new=empty)
#investigate reload function for home page with if statement for if something selected or not that way, you do everything in one html page.
@bp.route('/', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST':
        empty=False
        choice_dict = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
        cpu_chose = choice_dict[randrange(3)]
        return render_template('home.html',  selection = request.form['selection'],new = empty, cpu_select = cpu_chose)

#        if request.form['submit_button'] == 'Rock':
#            return render_template('Rock.html')
#        elif request.form['submit_button'] == 'Paper':
#            return render_template('Paper.html')
#        elif request.form['submit_button'] == 'Paper':
#            return render_template('Scissors.html')
    else:
        pass # unknown
 
