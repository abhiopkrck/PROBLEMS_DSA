n=int(input("Enter a number:"))

# largest=0

smallest=n

# while n!=0:
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     n=n//10
# print(" The largest digit is:",largest)

while n!=0:
    digit=n%10
    if digit==0:
        smallest=digit
    elif digit < smallest:
        smallest=digit
    n=n//10

print(" The smallest digit is:",smallest)