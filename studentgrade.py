sum=0
print("enter the mark of six student")

for i in range(6):
    c=int(input("enter the marks"))
    sum=sum+c
    avg=sum/6
print(sum)
print(avg)
if(avg>50):
    print("your grade is A")
elif(avg<50 and avg>40):
    print("your grade is B")
elif(avg<40 and avg>30):
    print("your grade is C")
else:
    print("your grade is D")