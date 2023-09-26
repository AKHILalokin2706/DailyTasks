username = input("enter the username:")
password = int(input("enter the password:"))
username1 = input("enter the username again:")
password1 = int(input("enter the password again:"))
if(username1==username and password1==password):
    print("The credentials are same and login successful")
else:
    print("The credentails are not same and login failed")
