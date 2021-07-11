from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('rps',__name__)

@bp.route('/')
def home():
    return render_template('home.html', codes=session.keys())


