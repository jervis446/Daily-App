print 'sender'
t=raw_input("Enter y to continue to receive frames")
while t=="y":
    fopen=open("f1.txt","r")
    line=fopen.read()

    fopen.close()
    i=0
    while i<len(line):
        if line[i]!=" ":
            print "frame "+line+" received"
        i=i+1
    fopen=open("f2.txt","w")
    p=input("enter last ACK received\n")
    fopen.write(str(p))
    fopen.close()
    t=raw_input("Enter y to continue to receive frames")

        

