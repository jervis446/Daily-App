fropen=open("bytestuff.txt","r")
line=fropen.read()
fropen.close()
start=0
while True:
    start=line.find("dlestx",start)
    end=line.find("etx",start)
    start=start+1
    if start==-1 or end==-1:
        break
    print line[start+5:end-3]

