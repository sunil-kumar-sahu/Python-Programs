#Insert data to the table present in Sqlite DB
import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into student5 (st_name,st_class,st_email) VALUES
        ('Maneesh','BTech',"maneesh@gmail.com")
'''
conn.execute(ins)#it is used to execute the insert query
conn.commit()#it is used to commit the query
conn.close()