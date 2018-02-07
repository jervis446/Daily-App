
val1=raw_input('Input First operand: ') 
val2= raw_input ('Input Second operand: ')



def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst



	
def crc(a,b):
	bit1 = int(a,2)
	bit2 = int(b,2)
	print bit1
	print bit2
	g = []
	arr = len(b)	
    
	str = "x"+b;

	b=reverse(b)
	
	for i in range (0,arr):
		if (b[i]=='0'):
			g.append(0)
		else:
			g.append(int((bit1<<i)))
		
	res=int(g[0])
	for i in range (1,arr):
		res = int(res) ^ int(g[i])
	
	print "Result: "+bin(res)[2:].zfill(len(a)+len(b)-1)
	


	return res  



res=crc(val1,val2)



