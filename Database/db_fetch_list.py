from models import User


def start_application():
    db_fetch_all()
    print("[NOTICE] Running Function => [db_fetch_all]")


def db_fetch_all():
    users_list = User.query.order_by(
        User.user_register_date.desc()).limit(20).all()
    print("[CONSOLE] Running DB Fetch Listing => [%s]" % str(users_list))


def main():
    print("--------------------[RUNNING]--------------------")
    start_application()
    print("--------------------[RUNNING]--------------------")


if __name__ == '__main__':
    main()
