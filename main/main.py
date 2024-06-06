import sqlite3

connection = sqlite3.connect("db/example.db")

print(connection.total_changes)