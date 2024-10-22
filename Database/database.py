import sqlite3

conn = sqlite3.connect("univ.db")

cur = conn.cursor()

cur.execute('create table students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references dept(deptno))')

conn.commit()

cur.close()

conn.close()