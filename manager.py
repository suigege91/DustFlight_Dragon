from main import app
from Database.models import db, User, Post
from flask_restful import Api, Resource
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

api = Api(app)
manager = Manager(app)
migrate = Migrate(app)

manager.add_command("s", Server())
manager.add_command("server", Server())
manager.add_command("runserver", Server())
manager.add_command("db", MigrateCommand)


def start_application():
    db_generator()
    print("[CONSOLE] DB Generator => [db_generator] Successfully")


class API_Service_View(Resource):
    def get(self):
        return {
            "welcome_message": {
                "Hello": ["Welcome to DustFlight VNS API Service", "Powered By DustFlight_Ryan"]
            }
        }


class Quotes(Resource):
    def get(self):
        return {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
                          'Some are born great, some achieve greatness, and some greatness thrust upon them.']
            },
            'Linus': {
                'quote': ['Talk is cheap. Show me the code.']
            }
        }


class API_DB_Fetch_All(Resource):
    def get(self):
        collection_space = []
        users_list = User.query.order_by(User.user_register_date.desc()).all()
        print("[CONSOLE] Running DB Fetch Listing => [%s]" % str(users_list))
        for user in users_list:
            collection_space.append(user.to_json())
        return {"users_list": collection_space}


api.add_resource(API_Service_View, '/api/index')
api.add_resource(Quotes, '/api/quotes')
api.add_resource(API_DB_Fetch_All, '/api/db_fetch_all')


@manager.shell
def system_shell_context():
    return dict(app=app,
                db=db,
                user=User,
                post=Post, )


def db_generator():
    print("-------------[WARNING - DB Generating now]-------------")
    db.create_all()
    print("-------------[WARNING - DB Generating now]-------------")


def main():
    print("=====================[RUNNING_NOW]=====================")
    start_application()
    manager.run()
    print("=====================[RUNNING_NOW]=====================")


if __name__ == '__main__':
    main()
