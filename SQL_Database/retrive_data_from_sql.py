import sqlite3
# Estblish connection and cursor
con = sqlite3.connect('database.db')
cur = con.cursor()


#GET ALL ROWS AND COLUMNS BY ORDER OF ASN
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall())


#GET ALL ROWS WITH ESPECIFIED COLUMNS
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())

#CONDITIONALS
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall())

#CONDITIONALS
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall())