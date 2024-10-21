import sqlite3
import pandas

con = sqlite3.connect("database.db")
cur =  con.cursor()

df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

df.to_csv('database.csv', index=False)

#pip install openpyxl
df.to_excel('database.xlsx', index=False)

df2 = pandas.read_excel('database.xlsx')
print(df2)