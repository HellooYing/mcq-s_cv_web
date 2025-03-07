from settings import settings,is_closing,signal_handler,try_exit
from model import MainHandler,UploadHandler,UploadCHandler,UploadKHandler
import tornado.ioloop
import signal
from tornado.options import options
import pymysql
import torndb
import function as fc

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/upload", UploadHandler),
    (r"/uploadc", UploadCHandler),
    (r"/uploadk", UploadKHandler),
], **settings)

application.db = torndb.Connection(
        host='127.0.0.1',
        database='mcqcv',
        user='root',
        password='12qwaszx'
    )
if __name__ == "__main__":
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    application.listen(8888)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
    tornado.ioloop.IOLoop.instance().start()