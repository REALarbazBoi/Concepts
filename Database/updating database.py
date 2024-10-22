import sqlite3
 
 
conn = sqlite3.connect('shop.db')
 
cur = conn.cursor()
 
customers = [
                [101, "Anita", "Delhi"],
                [102, "Raj", "Hyderabad"],
                [103, "Michael", "Kolkata"],
                [107, "Ali", "Delhi"],
                [109, "Sharma", "Chennai"],
            ]
 
products = [
                [10, "Toothpaste", 20],
                [11, "Toothbrush", 10],
                [12, "Lotion", 30],
                [13, "Shampoo", 25],
                [14, "Soap", 10],
            ]
 
orders = [
                [10005, 101, 10, 1],
                [10005, 101, 11, 2],
                [12389, 109, 12, 1],
                [12389, 109, 14, 1],
                [12389, 109, 11, 2],
                [63017, 103, 13, 4],
                [63017, 103, 10, 1],
                [63017, 103, 11, 4],
                [71222, 101, 12, 2],
                [71222, 101, 13, 1],
                [96351, 102, 14, 1],
            ]
 
 
for c in customers:
     cur.execute(f"INSERT INTO Customer Values({c[0]},'{c[1]}','{c[2]}')")
 
for p in products:
     cur.execute(f"INSERT INTO Product Values({p[0]},'{p[1]}','{p[2]}')")
 
for o in orders:
     cur.execute(f"INSERT INTO Orders Values({o[0]},{o[1]},{o[2]},{o[3]})")
 
conn.commit()
cur.close()
conn.close()