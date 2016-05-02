import sqlite3
import re

conn = sqlite3.connect('/Users/itlabs/db1.db')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS mega''')

cur.execute('''
CREATE TABLE mega (dates TEXT, people TEXT)''')

fname = '/tfs/report-MEGA.txt'

fh = open(fname)
count = 0
for line in fh:
    if not count % 2:
        #print "First", line
        people = line
        count = count + 1
        continue
    else:
        dates  = line.split()[2]
    alla = people, dates
    count = count + 1
    # Insert a row of data
    cur.execute("INSERT INTO mega VALUES (?,?)", alla)

    # Save (commit) the changes
    conn.commit()

sqlstr = 'SELECT dates, people FROM mega'

for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
