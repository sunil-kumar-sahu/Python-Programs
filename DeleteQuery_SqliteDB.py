import sqlite3
conn=sqlite3.connect("sqlite.db")
st_id=input("Enter the Student Id:-")
conn.execute("DELETE FROM student5 where st_id="+st_id)
conn.commit()
conn.close()