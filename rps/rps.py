from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('rps',__name__)
new = True

@bp.route('/')
def home():
    #set something to false here. then set it to true on the post part below
   return render_template('home.html', codes=session.keys())
#investigate reload function for home page with if statement for if something selected or not that way, you do everything in one html page.
@bp.route('/you-chose', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST':
        #I can probably add the refresh here. not actually refreshing. instead, I render the home page again but I have some sort of if statement for either case. when nothing is selected and for when something is selected.
        return render_template('you-chose.html',  selection = request.form['selection'])

#        if request.form['submit_button'] == 'Rock':
#            return render_template('Rock.html')
#        elif request.form['submit_button'] == 'Paper':
#            return render_template('Paper.html')
#        elif request.form['submit_button'] == 'Paper':
#            return render_template('Scissors.html')
    else:
        pass # unknown
 
