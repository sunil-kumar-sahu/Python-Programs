import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='school'
)
cursorobj=conn.cursor()
try:
    sql="Select * from student order by st_name ASC LIMIT 0,2"
    cursorobj.execute(sql)
    sdata=cursorobj.fetchall()
    for s in sdata:
        print(s)
except:
    print("Error...")