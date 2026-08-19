while True:
    try:
        age=int(input("Enter your age: "))
        if age >0:
            print("Age:",age)
            break
        else:
            print("Your age cannot be less than zero or negative")
    except ValueError:
        print("Please enter a Valid age")
