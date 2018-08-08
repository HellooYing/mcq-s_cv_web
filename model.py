import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("templates/index.html", title="My title", items=items)

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        if self.request.files.get('uploadfile', None):
            uploadFile = self.request.files['uploadfile'][0]
            filename = uploadFile['filename']
            fileObj = open("static/uoload/"+filename, 'wb')
            fileObj.write(uploadFile['body'])
        self.redirect('/')

class Upload2Handler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        file_metas = self.request.files["uploadfile"]
        for meta in file_metas:
            file_name = meta['filename']
            with open("static/uoload/"+file_name,'wb') as up:
                up.write(meta['body'])