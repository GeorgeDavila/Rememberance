import sqlite3

def dbinit(dbPATH):
    connection = sqlite3.connect(dbPATH)

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE processedscreengrab (grabid INTEGER, devicetime TIMESTAMP, ocrtext TEXT, classes TEXT, screenshot BLOB NOT NULL)")