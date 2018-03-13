import time
i=0
while(i<100):
    fil=open("Frame.txt","r")
    rec=fil.read()
    print rec
    fil.close()
    fil=open("Frame.txt","w").close()
    time.sleep(5)
    i=i+1
