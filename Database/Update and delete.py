# import sqlite3

# conn = sqlite3.connect("univ.db")

# curr = conn.cursor()

# rows = curr.execute("UPDATE DEPT SET name = 'Chem' where deptno = 40")

# conn.commit()

# new = curr.execute("select * from dept")


# print(new.fetchall())

# curr.close()

# conn.close()

# import sqlite3

# conn = sqlite3.connect("univ.db")

# curr = conn.cursor()

# rows = curr.execute("UPDATE Students SET city = 'Bhopal' where roll = 15")

# conn.commit()

# new = curr.execute("select * from students")


# print(new.fetchall())

# curr.close()

# conn.close()

# import sqlite3

# conn = sqlite3.connect("univ.db")

# curr = conn.cursor()

# rows = curr.execute("DELETE FROM Students where roll = 15")

# conn.commit()

# new = curr.execute("select * from students")


# print(new.fetchall())

# curr.close()

# conn.close()

import sqlite3

conn = sqlite3.connect("univ.db")

curr = conn.cursor()

rows = curr.execute("DELETE FROM dept where deptno = 40")

conn.commit()

new = curr.execute("select * from dept")


print(new.fetchall())

curr.close()

conn.close()
