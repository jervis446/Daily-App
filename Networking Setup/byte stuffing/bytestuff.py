t=int(raw_input('Enter the number of frames'))
final=""
fropen=open("bytestuff.txt","w")
while t>0:
    inp=raw_input("Enter the frame")
    final=final+"dlestx"+inp+"dleetx"
    t=t-1
fropen.write(final)
print final
