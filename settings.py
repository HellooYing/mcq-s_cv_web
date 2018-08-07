import tornado.ioloop
import logging
import os

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "debug":True,
}

is_closing = False

def signal_handler(signum, frame):
    global is_closing
    logging.info('exiting...')
    is_closing = True

def try_exit(): 
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()
        logging.info('exit success')