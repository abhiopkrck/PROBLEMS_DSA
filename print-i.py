n=int(input("Enter number:"))

result=1

for i in range(1,n+1):
    if n==1 or n==0:
        print("1")
    else:
        result *=i

print(f"The factorial of {n}:",result)