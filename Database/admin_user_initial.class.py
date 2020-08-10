from models import db, User


class DB_Initial():
    def __init__(self, user_name, user_pass, user_male, user_mail, user_address):
        self.user_name = user_name
        self.user_pass = user_pass
        self.user_male = user_male
        self.user_mail = user_mail
        self.user_address = user_address

    def db_user_addition(self):
        user = User(user_name=self.user_name, user_pass=self.user_pass, user_male=self.user_male,
                    user_mail=self.user_mail,
                    user_address=self.user_address)
        db.session.add(user)
        db.session.commit()


def main():
    user_name = "admin"
    user_pass = "admin"
    user_male = "man"
    user_mail = "suigege23@163.com"
    user_address = "China, Earth"
    db_initial = DB_Initial(user_name, user_pass, user_male, user_mail, user_address)
    db_initial.db_user_addition()


if __name__ == '__main__':
    main()
