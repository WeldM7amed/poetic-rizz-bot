import os
f = open('rizzourses.txt', 'r')
i = 0
directory = os.getcwd()
dir_path = directory+'\\subs'
os.mkdir(dir_path)
while True:
    line = f.readline()
    if not line:
        break
    line = line.strip()
    name="subs/" +str(i)+".srt"
    g = open(name,"w")
    txt = "1\n00:00:00,000 --> 00:00:09,000\n"+line
    g.write(txt)
    g.close()
    i=i+1
f.close()