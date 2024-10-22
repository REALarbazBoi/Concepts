import sqlite3

conn = sqlite3.connect("univ.db")

curr = conn.cursor()

for i in range(15):

    roll_no = int(input("enter the roll_no: "))

    name = input("enter the student name: ")

    city = input("enter the student city: ")

    deptno = int(input("enter the dept no: "))

    curr.execute(f'insert into students values({roll_no}, "{name}","{city}",{deptno})')

    conn.commit()


curr.close()

conn.close()