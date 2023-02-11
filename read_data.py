

 
def machine_7051(data):
    tmp1= bin(int(data[1:5], base=16))[2:]
    list1=(''.join(reversed(tmp1))) 
    T_Len=len(tmp1)
    for i in range(T_Len):
        list1+='0'
    return list1

def machine_7071Z(data):
    data=data.decode()
    spl1=data.split('>',1)
    spl2=spl1[1].split('\r',1)
    list1=spl2[0].split('+')
    return list1[1:]
'''
data1 = b'>+0.0065+0.0011+0.0065+0.0064+0.0064+0.0060+0.0037+0.5621+0.0029+0.0022+0.0011+0.0017+0.0020+0.4825+1.0000+1.0000+0.0114+0.0031+0.0018+0.0007\r'
test=machine_7071Z(data1)
print(test[0:])
'''