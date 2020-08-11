import os
import sys

sys.path.append(os.path.dirname(__file__) + os.sep + '../../')

from flask import Blueprint

basedir = os.path.abspath(os.path.dirname(__file__))

blog = Blueprint('blog', __name__, static_folder=os.path.join(basedir, 'static'),
                 template_folder=os.path.join(basedir, 'templates/Blog'))

from .views import *
