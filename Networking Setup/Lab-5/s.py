t=int(raw_input("enter the number of frames"))
fil=open("frames.txt","w+")
while (t>0):
    n=raw_input("enter the frames:")
    print n
    fil=open("frames.txt","a+")
    fil.write(str(n))
    fil.close()
    
