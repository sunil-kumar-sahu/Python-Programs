import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='school'
)
cursorobj=conn.cursor()
st_id=input("Enter the Student Id:-")

try:
    cursorobj.execute("DELETE  From student where st_id="+st_id)
    conn.commit()
    print("Student DELETED")
except:
    print("Error...")
