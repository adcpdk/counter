import sqlite3
import time
import urllib
import zlib
from dateutil.parser import parse

dict1 = {}
dict2 = {}
dict3 = {}
dicts = [dict1, dict2, dict3]

fin = {}

conn = sqlite3.connect('db1.db')
conn.text_factory = str
cur = conn.cursor()


orgs = ['adk', 'mega', 'sputnik']
print orgs
#for adk
asksql = list()
sqlstr = 'SELECT dates, people FROM adk'
sqlstr1 = 'SELECT dates, people FROM mega'
sqlstr2 = 'SELECT dates, people FROM sputnik'
asksql.append(sqlstr)
asksql.append(sqlstr1)
asksql.append(sqlstr2)

for base in range(3):
    for row in cur.execute(asksql[base]) :

        dictionary = dicts[base]

        people = row[1]
        people = int(people)

        dates = row[0]
        dates = dates.split()
        dates = dates[4:] + dates[1:3]
        dates = " ".join(dates)
        dt = parse(dates)
        dateform = str(dt.strftime('%Y-%m-%d'))
        #print dateform

        dictionary[dateform] = people
cur.close()

#print "LALALA", dict1
for i,b in dict1.items():
    print "Dict1: ",i,"people: ",b
for i,b in dict2.items():
    print "Dict2: ",i,"people: ",b
for i,b in dict3.items():
    print "Dict3: ",i,"people: ",b


dictionaries = [dict1.items(), dict2.items(),dict3.items()]
for i in range(3):
    for keyz, valuez in dictionaries[i]:
        if i ==0:
            fin[keyz] = str(valuez) + str("")
        elif i==1:
            if keyz not in fin.keys() :
                fin[keyz] = str(0) + str(",") + str(valuez) + str("")
            else:
                fin[keyz] = str(fin[keyz]) +","+ str(valuez)
        else:
            if keyz not in fin.keys() :
                fin[keyz] = str(0)+ str(",") + str(0) + str(",") + str(valuez) + str("")
            else:
                fin[keyz] = str(fin[keyz]) +","+ str(valuez)


#print fin
#for i,b in fin.items():
#    print "Final dictionary: ",i,b

#Start______________________________Cicle to add zeros that are missing
for keyq,valueq in fin.items():
    #print "JUST",keyq,valueq
    lessthen3 = 0
    for i in valueq.split(","):
        lessthen3 = lessthen3 + 1
    #print "Quantity: ",lessthen3
    if lessthen3 == 1:
        fin[keyq] = str(fin[keyq]) +","+ str(0) +","+ str(0)
    #print "After: ",fin[keyq]
    if lessthen3 == 2:
        fin[keyq] = str(fin[keyq]) +","+ str(0)
    #print "After: ",fin[keyq]
#End______________________________Cicle to add zeros that are missing

for i,b in fin.items():
    print "Final dictionary: ",i,b


fhand = open('gline.js','w')
fhand.write("gline = [ ['Month'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

# for month in months[1:-1]:
for i,b in sorted(fin.items()):
    fhand.write(",\n['"+i+"'")
    fhand.write(","+str(b))
    fhand.write("]");
fhand.write("\n];\n")


print "Data written to gline.js"
print "Open gline.htm in a browser to view"
