from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('rps',__name__)
empty = True 

@bp.route('/')
def home():
    #set something to false here. then set it to true on the post part below
   return render_template('home.html', codes=session.keys(), new=empty)
#investigate reload function for home page with if statement for if something selected or not that way, you do everything in one html page.
@bp.route('/', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST':
        empty=False
        return render_template('home.html',  selection = request.form['selection'],new = empty)

#        if request.form['submit_button'] == 'Rock':
#            return render_template('Rock.html')
#        elif request.form['submit_button'] == 'Paper':
#            return render_template('Paper.html')
#        elif request.form['submit_button'] == 'Paper':
#            return render_template('Scissors.html')
    else:
        pass # unknown
 
