import sqlite3
conn=sqlite3.connect("sqlite.db")
print("STUDENT ID","STUDENT NAME","STUDENT FEES")
data=conn.execute("SELECT f.st_id,s.st_name,f.fees_amount FROM fees_table as f left join student5 as s on f.st_id=s.st_id")
for a in data:
    print(a[0],a[1],a[2])
conn.close()