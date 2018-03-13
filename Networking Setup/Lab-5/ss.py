import time
import random
i=0
fil2=open("f2.txt","w")
k=1
fil2.write(str(k))
fil2.close()
while(i<100):
    fil1=open("f2.txt","r")
    rec=fil1.readline()
    if(rec=='1'):
        fil=open("f1.txt","w")
        k=input("enter the frames")
        print k
        fil.write(str(k))
        fil.close()
    fil1.close()
    time.sleep(5)
    i=i+1
    print 'Acknowledgement received'
