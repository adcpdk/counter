import sqlite3
import re
#CREATE TABLE Counts (dates TEXT, count INTEGER)
conn = sqlite3.connect('/Users/itlabs/db1.db')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS adk''')

cur.execute('''
CREATE TABLE adk (dates TEXT, people TEXT)''')

fname = '/tfs/report-ADK.txt'

fh = open(fname)
count = 0
for line in fh:
    if not count % 2:
        people = line
        count = count + 1
        continue
    else:
        dates  = line.split()[2]
    alla = people, dates
    count = count + 1
    # Insert a row of data
    cur.execute("INSERT INTO adk VALUES (?,?)", alla)

    # Save (commit) the changes
    conn.commit()

sqlstr = 'SELECT dates, people FROM adk'

for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
