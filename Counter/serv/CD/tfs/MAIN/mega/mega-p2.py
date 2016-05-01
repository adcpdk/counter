import os, time

localtime = time.asctime( time.localtime(time.time()) )
total=0
fread = open('./mega.txt')
readings=list()
for line in fread:
    readings.append(line)
    line = line.split()
    total = total + int(line[2])
fread.close()
to_write = str(localtime) + "\n" + readings[0] + "\n"
if os.path.exists("report-MEGA.txt"):
    '''f = file("report-MEGA.txt", "r+")
    f.write(tot)
    f.close()'''
    f = file("report-MEGA.txt", "a")
    f.write(to_write)
    f.close()
else:
    f = file("report-MEGA.txt", "w")
    f.write(to_write)
    f.close()
#f = file("./adk.txt", "w"),f.close()
#open('adk.txt', 'w').close()
os.remove("mega.txt")
