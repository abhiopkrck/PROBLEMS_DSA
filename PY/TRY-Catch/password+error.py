while True:
    password = input("Enter your password: ")

    has_number = False

    for char in password:
        if char.isdigit():
            has_number = True
            break

    if len(password) < 8:
        print("Password must be at least 8 characters")

    elif not has_number:
        print("Password must contain a number")

    else:
        print("Password accepted")
        break