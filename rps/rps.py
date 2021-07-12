from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('rps',__name__)

@bp.route('/')
def home():
    if request.method == 'POST':
    if request.form['submit_button'] == 'Rock':
        pass # do something
    elif request.form['submit_button'] == 'Paper':
        pass # do something else
    elif request.form['submit_button'] == 'Paper':
        pass # do something else
    else:
        pass # unknown
    return render_template('home.html', codes=session.keys())


