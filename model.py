import tornado.ioloop
import tornado.web
import json
import cnn
from cnn import car_type
from function import addimg
import pymysql
import torndb
from knn import pHash
import Levenshtein
db = torndb.Connection(
        host='127.0.0.1',
        database='mcqcv',
        user='root',
        password='12qwaszx'
    )

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("templates/index.html", title="My title", items=items)

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file_metas = self.request.files["uploadfile"]
        for meta in file_metas:
            file_name = meta['filename']
            with open("static/upload/"+file_name,'wb') as up:
                up.write(meta['body'])
            addimg(db,"static/upload/"+file_name,pHash("static/upload/"+file_name))
        self.redirect('/')

class UploadCHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        file_metas = self.request.files["uploadfile"]
        for meta in file_metas:
            file_name = meta['filename']
            with open("static/upload/"+file_name,'wb') as up:
                up.write(meta['body'])
        a=car_type("static/upload/"+file_name)
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
            with open("static/upload/"+file_name,'wb') as up:
                up.write(meta['body'])
        sql = 'SELECT * FROM img'
        all_img=db.query(sql)
        l=[]
        for i in all_img:
            b=pHash("static/upload/"+file_name)
            ll=[]
            ll.append(Levenshtein.distance(b,i.feature))
            ll.append(i.picture_address)
            if len(l)==0:
                l.append(ll)
            else:
                if ll[0]>l[-1][0]:
                    l.append(ll)
                else:
                    j=0
                    while(j<len(l)):
                        print(j)
                        if l[j][0]>=ll[0]:
                            l.insert(j,ll)
                            break
                        else:
                            j=j+1
                            
        response_data = {'imgs': l}
        self.write(json.dumps(response_data))
