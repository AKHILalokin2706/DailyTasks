list1=[]
while True:
    inp=input("enter the elements of the list one:")
    if inp=="":
        break
    else:
        list1.append(inp)
list2=[]
while True:
    inp2=input("enter the elements of the list two:")
    if inp2=="":
        break
    else:
        list2.append(inp2)

def to_dict(keys,values):
    return(dict(zip(keys,values)))
c=to_dict(list1,list2)
print(c)