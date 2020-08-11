import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(basedir)

from flask import Blueprint

dustflight_dragon = Blueprint('dustflight_dragon', __name__, static_folder='static',
                              template_folder='templates')

from .views import *
