import sqlite3

conn = sqlite3.connect('orders.db')

cur = conn.cursor()

cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

cur.execute("""CREATE TABLE IF NOT EXISTS authors(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS books(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

moreShows = [('Money Heist', 'Alex Rodrigo', 2017),
            ('Dark', 'Baran bo Odar', 2017),
            ('1992 Scam', 'Hansal Mehta', 2020)]

