


while True:
    try:
        content = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Please enter a number")


print(content)