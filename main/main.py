import sqlite3

connection = sqlite3.connect("db/user.db")

print(connection.total_changes)