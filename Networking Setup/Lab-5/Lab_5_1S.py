import time
i=0
fil=open("Frame.txt","w+")
while(i<100):
    n=input("enter the frame:")
    print n
    fil=open("Frame.txt","a+")
    fil.write(str(n))
    fil.close()
    time.sleep(5)
    i=i+1
    
