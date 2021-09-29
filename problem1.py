##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
a=0
atemp= True
while atemp:
    x = input("Enter username=>").strip()
    if x == "admin":
        y = input("Enter password=>").strip()
        if y== "12345":
            print("Access granted")
            atemp= False
        else:
            print("Access denied")
            a= a+1
            if a == 3:
                print("Too many failed attempts. Access denied.")
                atemp= False
    else:
        print("Access denied")
        a= a+1
        if a ==3:
            print("Too many failed attempts. Access denied.")
            atemp= False

