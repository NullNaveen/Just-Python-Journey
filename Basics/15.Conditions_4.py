UserName = input("Enter your Username: ")
MyList = ["hi", "wow", "this is it!"]

if UserName in MyList:
    print("The given user name already exists")

if len(UserName)<10:
    print("Username contains less than 10 characters")
elif len(UserName)==10:
    print("You are good to go")
else:
    print("done")
