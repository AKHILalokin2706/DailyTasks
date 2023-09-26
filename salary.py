emp_id=int(input("enter the Employeeid"))
emp_name=input("enter the employeename")
basic_pay=int(input("enter the basic pay"))
if(basic_pay>10000):
    hra=((15/100)*basic_pay)
    print(hra)
    da=((8/100))
    print(da)
    net_pay=basic_pay+hra+da
    print(net_pay)
elif(basic_pay<10000 and basic_pay>=5000):
    hra=((10/100)*basic_pay)
    print(hra)
    da=((5/100)*basic_pay)
    print(da)
    net_pay=basic_pay+hra+da
    print(net_pay)
else:
    hra=((5/100)*basic_pay)
    print(hra)
    da=((3/100)*basic_pay)
    print(da)
    net_pay=basic_pay+hra+da
    print(net_pay)