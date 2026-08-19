while True:
    try:
        num1=int(input("Enter a number 1:"))
        num2=int(input("Enter a number 2:"))
        div=num1/num2
    except ValueError:
        print("Enter valid number")
    except ZeroDivisionError:
        print("You Cannot Divide by 0")
    else:
        print(("The Result is:",div))
        break

print("Program finished")