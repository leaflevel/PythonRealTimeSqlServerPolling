import datetime
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-KJ7TKBR\\SQLEXPRESS;'
                      'Database=Python;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

minrid = 0

while 1==1:
    cursor.execute(f"SELECT rid, Random, DateTime FROM python..realtimelog where rid > {minrid}")
    for row in cursor:
        rid = row[0]
        t=row[2]
        r = row[1]

        print(f"{minrid},{rid}, {r}, {t}")
        minrid = minrid+rid
        #print(f'minrid is now: {minrid}')
        if rid == 100: break





