import tornado.ioloop
import tornado.web
import json
import classifier
from classifier import car_type

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

class UploadCHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        file_metas = self.request.files["uploadfile"]
        for meta in file_metas:
            file_name = meta['filename']
            with open("static/uoload/"+file_name,'wb') as up:
                up.write(meta['body'])
        a=car_type("static/uoload/"+file_name)
        if int(a)==0:
            imgs="/static/car-type-classifier/data/car_photos/ygc/ygc1.jpg"
            car="油罐车"
        elif int(a)==1:
            imgs="/static/car-type-classifier/data/car_photos/dhc/dhc1.jpg"
            car="大货车"
        elif int(a)==2:
            imgs="/static/car-type-classifier/data/car_photos/xhc/xhc1.jpg"
            car="小货车"
        elif int(a)==3:
            imgs="/static/car-type-classifier/data/car_photos/jc/jc1.jpg"
            car="小轿车"
        elif int(a)==4:
            imgs="/static/car-type-classifier/data/car_photos/kc/kc1.jpg"
            car="大客车"
        else:
            print("!!!")
        response_data = {'imgs': imgs,'car':car}
        self.write(json.dumps(response_data))

class UploadKHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        file_metas = self.request.files["uploadfile"]
        for meta in file_metas:
            file_name = meta['filename']
            with open("static/uoload/"+file_name,'wb') as up:
                up.write(meta['body'])
        response_data = {'imgs': file_name}
        self.write(json.dumps(response_data))
