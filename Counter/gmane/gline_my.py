import sqlite3
import time
import urllib
import zlib
from dateutil.parser import parse
#from sortedcontainers import SortedDict
y=0
z=0

#orgs = sorted(sendorgs, key=sendorgs.get, reverse=True)
#import re
#for adk

dict1 = {}
dict2 = {}
dict3 = {}

fin = {}

conn = sqlite3.connect('db1.db')
conn.text_factory = str
cur = conn.cursor()

# Determine the top ten organizations
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
counts = dict()
peoples = dict()
months = list()
count_list = list()
count_list1 = list()
count_list2 = list()

dicts = [dict1, dict2, dict3]
#print dicts[0]
for base in range(3):
    for row in cur.execute(asksql[base]) :
        #people
        dictionary = dicts[base]
        people = row[1]
        people = int(people)
        #dates
        dates = row[0]
        dates = dates.split()
        dates = dates[4:] + dates[1:3]
        dates = " ".join(dates)
        #print dates
        dt = parse(dates)

        #print(dt)
        # datetime.datetime(2010, 2, 15, 0, 0)
        #print(dt.strftime('%Y-%d-%m'))
        dateform = str(dt.strftime('%Y-%m-%d'))
        print dateform


        dictionary[dateform] = people
        #print base, "LOLOLO"
        #dictionaries = [dict1.items(), dict2.items()]
        '''for keyz, valuez in dicts[base]:
            if keyz not in fin.keys() :
                fin[keyz] = valuez
            else:
                fin[keyz] = fin[keyz],valuez

        #for i,b in fin.items():
        #    print i,b'''
        '''
        if dates not in months:
                months.append(dates)
        else: continue
        #ending dates, months should have all dates

        key = dates
        x = people

        counts.setdefault(key, [])
        counts[key].append(x)
        #counts[key].append(a)
        #counts[key].append(b)
        #print "############",counts, "#############"
        #print ":::::::::::::::::::::::::::",counts.get(key)
        count_list.append(x)'''
        #count_list1.append(a)
        #count_list2.append(b)

        #print dates
        #print people
    #print "Data in months: ",months
    #print "Data in count_list strts here: ",count_list, "ends here!"
cur.close()
print "LALALA", dict1
for qo,eo in dict1.items():
    print "Dict1: ",qo,"people: ",eo
for qa,ea in dict2.items():
    print "Dict2: ",qa,"people: ",ea
for qs,es in dict3.items():
    print "Dict3: ",qs,"people: ",es

#all_dict_list = [dict1.items(), dict2.items(), dict3.items()]


#final_dict_all = {}
#for i in all_dict_list:
#    final_dict[0] = all_dict_list




dictionaries = [dict1.items(), dict2.items(),dict3.items()]
for i in range(3):
    for keyz, valuez in dictionaries[i]:
        if i ==0:
            fin[keyz] = str(valuez) + str("")
        elif i==1:
            if keyz not in fin.keys() :
                #fin[keyz] = fin.get(valuez, 0) +1
                fin[keyz] = str(0) + str(",") + str(valuez) + str("")
                #if fin[keyz] is None:
                #    fin[keyz] = str(valuez) + str("")
            else:
                #fin[keyz] = 7
                fin[keyz] = str(fin[keyz]) +","+ str(valuez)
        else:
            if keyz not in fin.keys() :
                #fin[keyz] = fin.get(valuez, 0) +1
                fin[keyz] = str(0)+ str(",") + str(0) + str(",") + str(valuez) + str("")
                #if fin[keyz] is None:
                #    fin[keyz] = str(valuez) + str("")
            else:
                #fin[keyz] = 7
                fin[keyz] = str(fin[keyz]) +","+ str(valuez)


print fin
for i,b in fin.items():
    print "Final dictionary: ",i,b


for keyq,valueq in fin.items():
    print "JUST",keyq,valueq
    lessthen3 = 0
    for i in valueq.split(","):
        lessthen3 = lessthen3 + 1
    print "Kolichestvo: ",lessthen3
    if lessthen3 == 1:
        fin[keyq] = str(fin[keyq]) +","+ str(0) +","+ str(0)
    print "After: ",fin[keyq]
    if lessthen3 == 2:
        fin[keyq] = str(fin[keyq]) +","+ str(0)
    print "After: ",fin[keyq]
for i,b in fin.items():
    print "ZZFinal dictionary: ",i,b
#d = {2:3, 1:89, 4:5, 3:0}
#s = SortedDict(fin)
#print s.items()
#for key in sorted(fin):
#    print ((parse(key).strftime('%Y-%d-%m')), fin[key])
#fin((v,k) for k,v in enumerate(calendar.month_abbr))
#dt = parse('2016 Mar 19')
#print(dt)
# datetime.datetime(2010, 2, 15, 0, 0)
#print(dt.strftime('%Y-%d-%m'))
# 15/02/2010
"""for key,value in sorted(fin.items()):
    print key,value"""
'''
for i in fin.values():
    not_more_then3 = 0

    print i.split(",")
    for nmt3 in i.split(","):
        not_more_then3 = not_more_then3 + 1
    print not_more_then3
    if not_more_then3 == 1:
        #i.split(",").append("0")
        print "Appending #,0,0"
    elif not_more_then3 == 2:
        print "Appending #,#,0"
print fin.values()[0][:4]
print fin[fin.keys()[0]]
print fin.values()
'''
#print

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


#__dic_test
#print "Counts starts here: ",counts,"Ends here"
'''fhand = open('gline.js','w')
fhand.write("gline = [ ['Month'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")
for month in months:
    fhand.write(",\n['"+month+"'")
    fhand.write(","+str(count_list[y]))
    #fhand.write(","+str(count_list1[y]))
    #fhand.write(","+str(count_list2[y]))
    fhand.write("]");
    y = y + 1
fhand.write("\n];\n")'''
# for month in months[1:-1]:

print "Data written to gline.js"
print "Open gline.htm in a browser to view"
