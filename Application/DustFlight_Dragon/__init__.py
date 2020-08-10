import sys

sys.path.append("../../")

from flask import Blueprint

# dustflight_dragon = Blueprint('dustflight_dragon', __name__, static_folder='../../static',
#                               template_folder='../../templates')


dustflight_dragon = Blueprint('dustflight_dragon', __name__, static_folder='static',
                              template_folder='templates')

from .views import *
