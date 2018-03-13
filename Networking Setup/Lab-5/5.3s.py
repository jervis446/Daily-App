sent,l=0,1
t=raw_input("Enter y to continue to transmit frames")
while t=="y":
    c=1

    tframes=raw_input("Enter total number of frames")
    while (c==1):
        i=0
        final=""
        while i<int(tframes):
            print " frame ",
            print sent,
            print " has been transmitted\n"
            final=final+" "+str(sent)
            sent=sent+1
            i=i+1
            if sent==int(tframes):
                break
            fopen=open("f1.txt","w")

            fopen.write(final)
            fopen.close()
            try:
                fopen=open("f2.txt","r")
                #print final
                ack=fopen.read()
                if ack=="":
                    c=1
                elif ack==tframes:
                    c=2
                    break
                else:
                    sent=int(ack)
            except:
                 print "waiting\n"
            t=raw_input("Enter y to continue to send frames")








