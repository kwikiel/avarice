import psycopg2
from invest import Investor


jow = Investor("", None)
try:
    conn = psycopg2.connect("dbname='ostr' user='kacper' host='localhost' password='xD'")
    print("Connected")
    cur = conn.cursor()
    cur.execute('SELECT * FROM investments WHERE "investorId"=6736')
    rows = cur.fetchall()
    for row in rows:
        jow.delete(row[0])
except:
    print("UNABLE TO CONNECT")
