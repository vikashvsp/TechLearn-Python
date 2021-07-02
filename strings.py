import re

full_name=input("Enter your First Name:- ")
email=input("Enter your Email ID:- ")
phone=input("Enter your phone number:- ")
password=input("Enter your password:- ")
if(re.fullmatch('[A-Za-z0-9._%+]{1,20}@[A-Za-z0-9._]{2,20}\.[A-Za-z]{2,3}',email)):    print("Valid Email ID")
else:    print("invalid Email ID")
if(re.fullmatch('[0-9]{10}',phone)):
    print("Valid Phone Number")
else:
    print("Invalid Phone number")
if(len(password)>=8):
    if(re.search('[A-Z]',password)):
        if(re.search('[0-9]',password)):
            if(re.search('[_&@$#]',password)):
                print("Valid password")
            else: print("Invalid password")
        else: print("Invalid password")
    else: print("Invalid password")
else: print("Invalid password")
name=full_name.strip()
first_name,last_name=name.split(" ")
print("First name= ",first_name)
print("Last name= ",last_name)
username1="._.".join([first_name,last_name])
username=re.sub('a','@',username1,flags=re.IGNORECASE)
print("User Name= ",username)