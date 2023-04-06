#Connect to Database and create database
import mysql.connector
#Host->14.141.154.146
#Username->interns
#Password->interns@123
#port->3306
#DataBase->interns

myobj=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='bustable'
)
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")

except:
    print("database error..")
