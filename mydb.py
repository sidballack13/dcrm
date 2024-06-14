import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abcd@1234")

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("All done! Database created successfully!")