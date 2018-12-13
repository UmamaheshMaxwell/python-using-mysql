import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Olive123$"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
databaseExists = False

for database in mycursor.fetchall():
   if database[0] == 'TUTORIALS':
      databaseExists = True


if not databaseExists:
    mycursor.execute("CREATE DATABASE TUTORIALS")
else:
    print("Database already exists")