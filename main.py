from settings import settings,is_closing,signal_handler,try_exit
from model import MainHandler,LoginHandler
import tornado.ioloop
import signal
from tornado.options import options

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
], **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    application.listen(8888)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
    tornado.ioloop.IOLoop.instance().start()