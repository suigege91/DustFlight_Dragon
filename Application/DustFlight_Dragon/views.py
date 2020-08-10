from . import dustflight_dragon
from flask import render_template
from datetime import datetime


@dustflight_dragon.route('/')
@dustflight_dragon.route('/home')
def home():
    # return render_template('/DustFlight_Dragon/index.html',
    #                        title='Home Page',
    #                        year=datetime.now().year, )

    return "<h1>DustFlight - Visual Studio HOME</h1>"


@dustflight_dragon.route('/contact')
def contact():
    return render_template('/DustFlight_Dragon/contact.html',
                           title='Contact',
                           year=datetime.now().year,
                           message='Your contact page.')


@dustflight_dragon.route('/about')
def about():
    return render_template('/DustFlight_Dragon/about.html',
                           title='About',
                           year=datetime.now().year,
                           message='Your application description page.')
