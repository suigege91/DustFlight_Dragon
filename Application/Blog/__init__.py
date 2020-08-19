from flask import Blueprint


blog = Blueprint('blog', __name__, static_folder='../../static',
                 template_folder='../../templates/Blog')

from .views import *