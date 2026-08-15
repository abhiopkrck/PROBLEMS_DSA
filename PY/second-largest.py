n=int(input("Enter a number"))

largest=0
second_largest=0
while n!=0:
    digit=n%10
    if digit>largest:
        second_largest=largest
        largest=digit
    elif digit>second_largest:
        second_largest=digit
    n=n//10
print(largest)
print(second_largest)