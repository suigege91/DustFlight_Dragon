from models import db, Post


class DB_Initial():
    def __init__(self, post_title, post_content):
        self.post_title = post_title
        self.post_content = post_content

    def db_post_initial(self):
        post = Post(post_title=self.post_title, post_content=self.post_content)
        db.session.add(post)
        db.session.commit()


def main():
    post_title = "DustFlight Virtual Network Studio"
    post_content = "Welcome to DustFlight VNS !"
    post_initial = DB_Initial(post_title, post_content)
    post_initial.db_post_initial()


if __name__ == '__main__':
    main()
