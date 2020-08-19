from flask import Flask
from Configuration.config import DevConfig, ProdConfig, db
from Application.Blog import blog

app = Flask(__name__)
app.config.from_object(DevConfig)
app.register_blueprint(blog, url_prefix='/blog')
db.init_app(app)


def start_application():
    welcome_information()
    print("[NOTICE] System Running Function => [welcome_information]")


def welcome_information():
    result_string = '''
        ###################################################################
        -------------------------------------------------------------------
        Welcome to DustFlight Virtual Network Studio ^_^
        -------------------------------------------------------------------
        ###################################################################
    '''


# @app.route('/set_session')
# def set_session():
#     session['data'] = 'DustFlight_VNS'
#     return "[CONSOLE] Session Setup Complete !"


@app.route("/")
@app.route("/index")
def index():
    return "<h1>DustFlight VNS - Welcome Page</h1>"


def main():
    my_host = "127.0.0.1"
    my_port = 9001
    print(
        "==========================[RUNNING_PROCESSING]==========================")
    start_application()
    print("------------------------------------------------------------------------")
    print(app.url_map)
    print("------------------------------------------------------------------------")
    app.run(host=my_host, port=my_port)
    print(
        "==========================[RUNNING_PROCESSING]==========================")


if __name__ == '__main__':
    main()
