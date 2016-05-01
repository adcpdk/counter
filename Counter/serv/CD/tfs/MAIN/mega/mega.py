import os

try:
    readings = list()
    fread = open('./mega.txt')
    for line in fread:
        line = line.split()
        line = line[2]
        readings.append(line)
    fread.close()
    fwrite = open('./mega.txt','w')
    xori = readings[0]
    xori = int(xori)
    xori = xori + 1
    textADK = 'MEGA = ' + str(xori)
    fwrite.write(textADK)
    fwrite.close()
except IOError:
    print "file not found"
    f = file("./mega.txt", "w")
    textADK = 'MEGA = 0'
    f.write(textADK)
    f.close()
    fread = open('./mega.txt')
    for line in fread:
        line = line.split()
        line = line[2]
        readings.append(line)
    fread.close()
    fwrite = open('./mega.txt','w')
    xori = readings[0]
    xori = int(xori)
    xori = xori + 1
    textADK = 'MEGA = ' + str(xori)
    fwrite.write(textADK)
    fwrite.close()
