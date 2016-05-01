import os, time

localtime = time.asctime( time.localtime(time.time()) )
total=0
fread = open('./adk.txt')
readings=list()
for line in fread:
    readings.append(line)
    line = line.split()
    total = total + int(line[2])
fread.close()
to_write = "\n" + str(localtime) + "\n" + readings[0] + ""
if os.path.exists("report-ADK.txt"):
    #trying to append to the report file if exists
    f = file("report-ADK.txt", "a")
    f.write(to_write)
    f.close()
else:
    #creatinga report file with the content
    f = file("report-ADK.txt", "w")
    f.write(to_write)
    f.close()

os.remove("adk.txt") #removing adk.txt to start a new day
