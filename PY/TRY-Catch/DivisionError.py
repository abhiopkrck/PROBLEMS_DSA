try:
    num1=int(input("Enter a number 1: "))
    num2=int(input("Enter a number 2: "))
    div=num1/num2
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("You Cant Division by zero")
else:
    print("The Result is:",div)
finally:
    print("The Division Is Done")