import pymysql
import torndb

def addimg(db,picture_address,feature_address):
    query = "INSERT into img (picture_address,feature_address) values (%s,%s)"
    term_id = db.execute_lastrowid(query,picture_address,feature_address)
    return term_id
