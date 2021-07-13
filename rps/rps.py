from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('rps',__name__)

@bp.route('/')
def home():
   return render_template('home.html', codes=session.keys())

@bp.route('/you-chose', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Rock':
            return render_template('Rock.html')
        elif request.form['submit_button'] == 'Paper':
            return render_template('Paper.html')
        elif request.form['submit_button'] == 'Paper':
            return render_template('Scissors.html')
    else:
        pass # unknown
 
