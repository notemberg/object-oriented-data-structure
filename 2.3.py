print("*** Odd Even ***")
sen = input("Enter Input : ")
type, data, mode = map(str,sen.split(','))

def odd_even(type, data, mode):
    newdata=[]
    if type.lower() == 'l': 
        newdata = data.split(" ")
    else:
        newdata = data

    if mode.lower() =='odd':
        return list(newdata[::2])
    elif mode.lower() =='even':   
        return list(newdata[1::2])


if type.lower() =='l':
    print(odd_even(type,data,mode))
elif type.lower()== 's':
    for vt in odd_even(type,data,mode):
        print(f"{vt}",end='')