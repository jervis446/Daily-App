print 'Sender Side Client Adarsh Kumar'
t, final=int(raw_input('Enter the Number of Frames : ')),""
fropen=open("amar.txt","w")
while t>0:
    frames=raw_input('Enter the Frames ')
    final=final+str(len(frames))+frames
    t=t-1
fropen.write(final)
fropen.close
print "Your Codeword that Generate "+final
