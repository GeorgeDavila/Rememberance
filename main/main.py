import os
from utils.sqldb_setup import *
from utils.sqldb_funcs import *
import sqlite3
import datetime
from PIL import Image

userDB = "user.db"
db_directory = "db"
userDB_PATH = f"{db_directory}/{userDB}"

#ensure db exists on user device (since we gitignore it)
existingDBs = os.listdir(db_directory)
if userDB not in existingDBs:
    dbinit(userDB_PATH)

grabid = 1
devicetime = datetime.datetime.now()
ocrtext = "Hello world!"
classes = "placeholder"

screenshotPATH = "testimg1.jpg" #might just temp save screenshots as temp.png alternative is to save to sql from pil/cv2 image object

connection = sqlite3.connect(userDB_PATH)
insertBLOB(grabid, devicetime, ocrtext, classes, screenshotPATH, userDB_PATH)
print(connection.total_changes)