from settings import settings,is_closing,signal_handler,try_exit
from model import MainHandler,UploadHandler,Upload2Handler
import tornado.ioloop
import signal
from tornado.options import options

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/upload", UploadHandler),
    (r"/upload2", Upload2Handler),
], **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    application.listen(8888)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
    tornado.ioloop.IOLoop.instance().start()