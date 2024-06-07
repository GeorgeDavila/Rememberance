import sqlite3

connection = sqlite3.connect("db/user.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE post_ocr (name TEXT, textonscreen TEXT, classes TEXT, localdate DATE)")