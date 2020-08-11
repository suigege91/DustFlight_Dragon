import os
import sys

sys.path.append(os.path.dirname(__file__) + os.sep + '../')

from . import app
from Blog import blog
from flask import render_template
from flask_restful import Api, Resource

api = Api(app)


@blog.route('/')
@blog.route('/index')
def index():
    tempalte_html = "index.html"
    template_title = "DustFlight VNS Dragon - Blog _ Index"
    template_content = "Welcome to DustFlight Dragon - Blog System"
    return render_template(tempalte_html, title=template_title, content=template_content)

    # return template_content


class API_DB_Fetch_All(Resource):
    def get(self):
        collection_list = []
        users_list = User.query.order_by(
            User.user_register_date.desc()).limit(20).all()
        print("[CONSOLE] Running DB Fetch Listing => [%s]" % str(users_list))
        for user in users_list:
            collection_list.append(user.to_json())
        return {"stories": collection_list}


api.add_resource(API_DB_Fetch_All, '/api/db_fetch_all')
