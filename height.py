height=int(input("enter the height in cm:"))
if(height<=0):
    print("The height entered by the user is invalid:")
else:
    inchheight=(height/2.54)
    print(inchheight)