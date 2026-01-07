# db.py
import pymysql

def get_db():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        database="webapp",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
