def calculation(a,b):
    addition=a+b
    Subtraction=a-b
    Multiplication=a*b
    Division=a/b
    return addition,Subtraction,Multiplication,Division

addition,Subtraction,Multiplication,Division=calculation(3,4)
print(f"Addition:{addition}")
print(f"Subtraction:{Subtraction}")
print(f"Multiplication:{Multiplication}")
print(f"Division:{Division}")