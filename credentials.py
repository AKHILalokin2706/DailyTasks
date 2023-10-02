username = input("Enter username: ")
password = input("Enter password: ")

entered_username = input("Re-enter username: ")
entered_password = input("Re-enter password: ")

if username == entered_username and password == entered_password:
    print("Login successful!")
else:
    print("Incorrect username or password. Please try again.")
