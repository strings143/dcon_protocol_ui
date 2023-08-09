#讀取機台data做切割，傳給controller.py檔
def machine_7051(data):
    try:
        tmp1= bin(int(data[1:5], base=16))[2:]
        list1=(''.join(reversed(tmp1))) 
        T_Len=len(tmp1)
        for i in range(T_Len):
            list1+='0'
        return list1
    except Exception as e:
        print("錯誤:",e)
def machine_7071Z(data):
    try:
        data=data.decode()
        spl1=data.split('>',1)
        spl2=spl1[1].split('\r',1)
        list1=spl2[0].split('+')
        return list1[1:]
    except Exception as e:
        print("錯誤:",e)