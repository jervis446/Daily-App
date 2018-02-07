
def xor(a, b):
 
 
    result = []
 
 
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)
 
def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst


def mod2div(divident, divisor):
 
    
    pick = len(divisor)
 
    
    tmp = divident[0 : pick]
 
    while pick < len(divident):
 
        if tmp[0] == '1':
 
          
            tmp = xor(divisor, tmp) + divident[pick]
 
        else:   
            tmp = xor('0'*pick, tmp) + divident[pick]
 
       
        pick += 1
 
  
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword
 

def encodeData(data, key):
 
    l_key = len(key)
 
   
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    
    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Encoded Data (Data + Remainder) : ",
          codeword)
 

data = "1101"
key = "11001011"

key=reverse(key)
encodeData(data, key)
