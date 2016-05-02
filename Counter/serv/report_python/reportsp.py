import sqlite3
import re
#CREATE TABLE Counts (dates TEXT, count INTEGER)
conn = sqlite3.connect('/Users/itlabs/db1.db')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS sputnik''')

#cur.execute('''
#CREATE TABLE Counts (email TEXT, count INTEGER)''')

cur.execute('''
CREATE TABLE sputnik (dates TEXT, people TEXT)''')

fname = '/tfs/report-Sputnik.txt'

fh = open(fname)
#people = None
count = 0
for line in fh:
    #print line
    #if not line.startswith('From: ') : continue

    #z = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
    #za = re.findall(('@(\S+)'),z)
    #print '\n', za
    #datesanization = line.findall('^From:.*@(\S+)')
    #print line

    #dates = line
    #people = line
    if not count % 2:
        #print "First", line
        people = line
        count = count + 1
        continue
    else:
        #print "Second", line
        dates  = line.split()[2]
    #print dates
    #print "data", dates
    '''if line.startswith('ADK') :
        line=line.split()
        #print "#############", line[2]
        people = line[2]
        print "########", people
    else:
        dates = line'''


    alla = people, dates
    count = count + 1
    #pieces = line.split()
    #email = pieces[1]
    #email1 = str(email)
    #print email1.split('@')[1]
    #dates = email1.split('@')[1]
    #print email
    #datesanization = email1.findall('@(\S+)')
    #print datesanization
    # Create table


    # Insert a row of data
    cur.execute("INSERT INTO sputnik VALUES (?,?)", alla)

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.



# https://www.sqlite.dates/lang_select.html
sqlstr = 'SELECT dates, people FROM sputnik'

#sqlstr = 'SELECT dates, count, people FROM sputnik ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
