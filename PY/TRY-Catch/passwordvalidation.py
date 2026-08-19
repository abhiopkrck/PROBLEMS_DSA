while  True:
    password=input("Enter your password: ")
    if len(password)>=8:
        print("Your password is valid")
        break
    else:
        print("Your password is not valid")