import time
i=0
while(i<100):
    fil=open("f1.txt","r")
    rec=fil.readline()
    print rec
    if(int(rec)!='\0'):
        fil1=open("f2.txt","w")
        k=1
        fil1.write(str(k))
        fil1.close()
    fil.close()
    fil=open("f1.txt","w").close()
    time.sleep(5)
    i=i+1 
