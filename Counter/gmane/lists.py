dict1={"a":1, "b":2}
dict2={"c":3, "a":5}
dict3={"c":4, "r":12}
dict4={"c":5}
list_of_dict = [dict1,dict2,dict3, dict4]
final_dict = {}
for i in range(4):
    #print i
    if i == 0:
        for key,value in dict1.items():
            #print key, value
            final_dict[key] = value
    else:
        for key,value in list_of_dict[i].items():
            if key in final_dict.keys():
                final_dict[key] = final_dict[key], value
            else:
                print final_dict.get(key,0)
                final_dict[key] = 0,value
    #elif i == 2:

print final_dict
for a,b in final_dict.items():
    print a,b
orgs
fhand = open('gline.js','w')
fhand.write("gline = [ ['Month'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

# for month in months[1:-1]:
for month in months:
    fhand.write(",\n['"+month+"'")
    for org in orgs:
        key = (month, org)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")

print "Data written to gline.js"
print "Open gline.htm in a browser to view"
