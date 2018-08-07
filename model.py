import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("templates/index.html", title="My title", items=items)

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")