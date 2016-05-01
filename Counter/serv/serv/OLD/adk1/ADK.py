import os

try:
    readings = list()
    fread = open('./adk.txt')
    for line in fread:
        line = line.split()
        line = line[2]
        readings.append(line)
    fread.close()
    fwrite = open('./adk.txt','w')
    xori = readings[0]
    xori = int(xori)
    xori = xori + 1
    textADK = 'ADK = ' + str(xori)
    fwrite.write(textADK)
    fwrite.close()
except IOError:
    print "file not found"
    f = file("./adk.txt", "w")
    textADK = 'ADK = 0'
    f.write(textADK)
    f.close()
    fread = open('./adk.txt')
    for line in fread:
        line = line.split()
        line = line[2]
        readings.append(line)
    fread.close()
    fwrite = open('./adk.txt','w')
    xori = readings[0]
    xori = int(xori)
    xori = xori + 1
    textADK = 'ADK = ' + str(xori)
    fwrite.write(textADK)
    fwrite.close()
