import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='school'
)
mycursor=conn.cursor()
try:
    #st_id,st_name,st_class,st_email
    ins="INSERT INTO student (st_name,st_class,st_email) values(%s,%s,%s)"
    t=[("sikan",'Bsc','sikan@gmail.com'),('Papun','BCA','papun@gmail.com')]#its for insert multiple row in a table
    mycursor.executemany(ins,t)
    conn.commit()
    print("Inserted Data Sucessfully")
except:
    print("Error...")