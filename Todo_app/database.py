import sqlite3


con = sqlite3.connect("mydata.db")

cur  = con.cursor()
cur.execute("create table task(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT)")
# cur.execute("create table student(id INTEGER PRIMARY KEY AUTOINCREMENT,fullname TEXT, email TEXT,password TEXT,address TEXT)")




con.commit()

con.close()