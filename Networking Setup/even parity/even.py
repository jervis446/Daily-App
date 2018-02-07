def sender():
    f=open("adarsh.txt","w+")
    dataword = str(input("Enter data word of 4 bit : "))
    if (len(dataword) > 4):
        print("Only 4 bit dataword is allowed")
    else:
        parity = dataword.count('1')
        dataword = list(dataword)   
    if(parity%2 == 0):
            dataword.append('0')
    else:
            dataword.append('1')
    for item in dataword:           
          f.write(item)
    f.close()      
    print(dataword) 


def receiver():
    filein = str(input("Enter file name"))
	
    f = open(filein, "r+")
    a = f.read()
    b = a.count('1')
    if (b%2 == 0):
        print(a[:-1])
    else:
        print("error detected resend frames")

		
sender()
receiver()