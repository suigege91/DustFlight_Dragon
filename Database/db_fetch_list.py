import sys

sys.path.append("../")
from main import app
from models import db, User, Post
from flask_restful import Api, Resource

api = Api(app)


def start_application():
    db_fetch_all()
    print("[NOTICE] Running Function => [db_fetch_all]")


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


def db_fetch_all():
    collection_list = []
    users_list = User.query.order_by(
        User.user_register_date.desc()).limit(20).all()
    for user in users_list:
        collection_list.append(user)
        print(collection_list)


def main():
    print("--------------------[RUNNING]--------------------")
    start_application()
    print("--------------------[RUNNING]--------------------")


if __name__ == '__main__':
    main()
