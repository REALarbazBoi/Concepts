# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("SELECT * FROM customer")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# find all customers from delhi

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("SELECT * FROM customer where address = 'Delhi'")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# find all the products with price greater than 20

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("select * from product where price > 20")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# Find all the product starting with "S"

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("select pname from product where pname like 'S%'")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# find the name of customers either living in delhi or chennai

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("select cname from customer where address in ('Delhi','Chennai')")

# rows = cur.execute("select cname from customer where address ='Delhi' or address ='Chennai'")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# Find order no and product no quantity greater than 1

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("select orderno, prodno from orders where orderno>1 and qty>1;")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# Find name of customer with order no 10005

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# # rows = cur.execute("select c.cname from orders as o join customer as c on c.custid=o.custid where orderno= 10005;")

# rows = cur.execute("select distinct c.cname from orders o, customer c where c.custid=o.custid and orderno=10005")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# Find product name and quantity in order number 63017

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()

# rows = cur.execute("select p.name, o.qty from orders as o, product as p where p.prodno=o.prodno and orderno=63017")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# Find order numbers which contains tootpaste

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()


# rows = cur.execute("select o.orderno from orders as o, product as p where o.prodno=p.prodno and p.pname='Toothpaste'")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()

# Find the names of the customer who purchased lotion

# import sqlite3

# conn = sqlite3.connect("shop.db")

# cur = conn.cursor()


# rows = cur.execute("select c.cname from customer as c, orders as o, product as p where (c.custid=o.custid and o.prodno=p.prodno) and p.pname='Lotion'")

# # conn.commit()

# print(rows.fetchall())

# cur.close()

# conn.close()