import pymssql

conn = pymssql.connect(host='127.0.0.1:1234', user='sa', password='test', database='DB001')
cur = conn.cursor()

cur.execute('SELECT getdate()')

a = cur.fetchall()

print(a[0][0])

cur.close()
conn.close()