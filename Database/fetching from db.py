import sqlite3

conn = sqlite3.connect("univ.db")

curr = conn.cursor()

rows = curr.execute("Select name, city from students where city in (select city from students where name = 'Verma')")

# allrows = rows.fetchall()

# for t in allrows:
#     print(t[0])

# conn.commit()

print(rows.fetchall())

curr.close()

conn.close()
