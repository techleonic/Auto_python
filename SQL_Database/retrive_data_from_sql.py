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

#CONDITIONALS ESPECIFIC
cur.execute("SELECT * FROM 'ips' WHERE asn = 144")
print(cur.fetchall())

#CONDITIONALS WITH AND EVERY CHARACTER THAT ENDS WITH SA
cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
results =  cur.fetchall()

#ITERATES
for rows in results:
    print(rows[1])
