import pymysql
import torndb

def addimg(db,picture_address,feature):
    query = "INSERT into img (picture_address,feature) values (%s,%s)"
    term_id = db.execute_lastrowid(query,picture_address,feature)
    return term_id
