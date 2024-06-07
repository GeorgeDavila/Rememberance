import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(grabid: int, devicetime, ocrtext: str, classes: str, screenshotPATH: str, dbPATH='db/user.db'):
    try:
        sqliteConnection = sqlite3.connect(dbPATH)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO processedscreengrab
                                  (grabid, devicetime, ocrtext, classes, screenshot) VALUES (?, ?, ?, ?, ?)"""

        screenshotData = convertToBinaryData(screenshotPATH)
        # Convert data into tuple format
        data_tuple = (grabid, devicetime, ocrtext, classes, screenshotData)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("data inserted successfully into table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(grabId, dbPATH='db/user.db'):
    try:
        sqliteConnection = sqlite3.connect(dbPATH)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from processedscreengrab where id = ?"""
        cursor.execute(sql_fetch_blob_query, (grabId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "captureTime = ", row[1])
            captureTime = row[1]

            print("Storing employee image and resume on disk \n")
            photoPath = "C:\db_data\\" + captureTime + ".png"
            writeTofile(captureTime, photoPath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
#insertBLOB(1, "Smith", "E:\pynative\Python\photos\smith.jpg", "E:\pynative\Python\photos\smith_resume.txt")
#insertBLOB(2, "David", "E:\pynative\Python\photos\david.jpg", "E:\pynative\Python\photos\david_resume.txt")