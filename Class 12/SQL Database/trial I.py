import MySQLdb
import tkinter

db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="DragonKing29",     # password
                     db="fairytail")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM examples")

# print the first and second columns      
for row in cur.fetchall() :
    print (row[0], " ", row[1])
