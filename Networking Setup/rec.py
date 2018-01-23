print "Receiver Side Aditya Priyam"
channel=raw_input('Enter the Channel Name(that is your txt) :')
fropen,i,c=open(channel,"r"),0,0
line=fropen.readline()
while i<len(line):
    print "Frame : ",
    k=int(line[i])
    if c!=0:
        print line[c:c+k]
    else:
        print line[1:c+k+1]
    i=i+k+1
    c=i+1
fropen.close
