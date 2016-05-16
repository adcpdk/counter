#dic_test.py
dict1 = {'01.02.2015' : 50, '02.02.2015' : 60}
dict2 = {'02.02.2015' : 10, '03.02.2015' : 70,'01.02.2015' : 55}
dict3 = {'02.02.2015' : 30}

fin = {}

'''for keyz, valuez in dict1.items():
    if keyz not in fin.keys() :
        fin[keyz] = valuez
    else:
        fin[keyz] = fin[keyz],valuez

#print "TOOOOOOOOOO", fin

for keyz, valuez in dict2.items():
    if keyz not in fin.keys() :
        fin[keyz] = valuez
    else:
        fin[keyz] = fin[keyz],valuez
    #print keyz, valuez

#printing stuff
#print "TOOOOOOOOOO", fin'''
dictionaries = [dict2.items(), dict1.items()]
for i in range(2):
    #print i
    for keyz, valuez in dictionaries[i]:
        #fin[keyz] = 0
        print keyz, i
        #if not keyz in fin.keys():
        #    fin[keyz] = 0
        if keyz not in fin.keys():
            #valuez = 0
#
            if i == 0:
                print "zuzu"
                fin[keyz] = valuez
            elif i == 1:
                print "kuku"
                fin[keyz] = str(fin[keyz]) + " 0 " + str(valuez)
        #elif keyz not in fin.keys() :
    #        fin[keyz] = 0

        else:
            print "OOOO"
            fin[keyz] = str(fin[keyz]) + " 0 " + str(valuez)
            #valuez = 0

            #fin[keyz] = str(fin[keyz]) + " " + str(valuez)
print "TTTTT"
adlist = []
for i,b in fin.items():
    print i,b
    adlist.append(b)
print adlist[0].split()[0]
