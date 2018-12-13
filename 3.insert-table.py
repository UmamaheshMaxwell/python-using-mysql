import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Olive123$",
    database="TUTORIALS"
)

myCursor = mydb.cursor()

