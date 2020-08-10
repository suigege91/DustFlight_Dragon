from main import app
from flask_script import Server, Manager
from Database.models import db, User, Post

manager = Manager(app)
manager.add_command("s", Server())
manager.add_command("server", Server())
manager.add_command("runserver", Server())


def start_application():
    db_generator()
    print("[CONSOLE] DB Generator => [db_generator] Successfully")


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
