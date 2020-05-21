import sqlite3
import os, sys

a = ['simsim', 'joljol ', ' ']

b = []
for i in a:
    str = i.strip()
    if len(str) == 0:
        i = None
        b.append(str)
    else:
        b.append(str)

fPath = os.getcwd()
fName = 'test.db'

if os.path.isfile(os.path.join(fPath, fName)):
    os.remove(os.path.join(fPath, fName))

conn = sqlite3.connect(os.path.join(fPath, fName))
cur = conn.cursor()

cur.execute("create table human(id int, man text);")

for i, data in enumerate(b):
    cur.execute("insert into human values (?, ?)",(i, data))

conn.commit()
conn.close()
