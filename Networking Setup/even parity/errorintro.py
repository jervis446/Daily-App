import random
channel=raw_input('Enter the channel name ')
fropen,i,c=open(channel,"rw+"),0,0
line=fropen.readline()
k=random.randint(1,10)
#print k
print line
line=str(k)+line[1:]
print line
fropen.write(line)


