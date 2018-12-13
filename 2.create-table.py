import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Olive123$",
    database="Tutorials"
)

mycursor = mydb.cursor()

# Chack if table exists
tableExists = False
mycursor.execute("SHOW TABLES")
for tables in mycursor.fetchall():
    if tables[0] == "customers":
        tableExists = True
createSqlQuery = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
if not tableExists:
    mycursor.execute(createSqlQuery)
    print("Table customers created sucessfully")
else:
    print("Table already exists !!")

# Alter the table with new column
columnExists = False
mycursor.execute("SHOW COLUMNs from customers")

for column in mycursor.fetchall():
    if (column[0] == "ID"):
        columnExists = True

if not columnExists:
    alterSqlQuery = "ALTER TABLE customers ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY"
    mycursor.execute(alterSqlQuery)
else:
    print('Column ID already exists !!!')

