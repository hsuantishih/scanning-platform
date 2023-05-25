import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

print(mydb)

# my_cursor = mydb.cursor("SHOW DATABASES")

# for db in my_cursor:
#     print(db)

