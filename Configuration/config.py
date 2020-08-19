import os
import gevent.monkey
import multiprocessing
from flask_sqlalchemy import SQLAlchemy

gevent.monkey.patch_all()

db = SQLAlchemy()


class Config(object):
    pass


class DevConfig(Config):
    debug = True
    SECRET_KEY = "DustFlight_Dragon_Secret_Key"

    # 数据库链接配置:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1q2w3e4r!@#@127.0.0.1:3306/dustflight_vns"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    debug = False
    """把session保存到redis中"""
    SECRET_KEY = "DustFlight_Dragon_Secret_Key"
    loglevel = 'debug'
    bind = "127.0.0.1:5000"
    pidfile = "../log/gunicorn.pid"
    accesslog = "../log/access.log"
    errorlog = "../log/debug.log"
    daemon = True
    # 启动的进程数
    workers = multiprocessing.cpu_count()
    worker_class = 'gevent'
    x_forwarded_for_header = 'X-FORWARDED-FOR'

    SESSION_TYPE = 'sqlalchemy'  # session的存储方式为sqlalchemy
    SESSION_SQLALCHEMY = db  # SQLAlchemy对象
    SESSION_SQLALCHEMY_TABLE = 'sessions'  # session要保存的表名称
    SESSION_PERMANENT = True  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀

    # session存储方式为redis
    # SESSION_TYPE="redis"
    # # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    # SESSION_PERMANENT = False
    # # 是否对发送到浏览器上session的cookie值进行加密
    # SESSION_USE_SIGNER = False
    # # 保存到redis的session数的名称前缀
    # SESSION_KEY_PREFIX = "session:"
    # # session保存数据到redis时启用的链接对象
    # SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置
