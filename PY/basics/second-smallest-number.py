
n=int(input("Enter a number:"))

smallest=n
second_smallest=n

while n!=0:
    digit=n%10
    if digit<smallest:
        second_smallest=smallest
        smallest=digit
    elif digit<second_smallest:
        second_smallest=digit
    n=n//10

print(f"Smallest is:{smallest}")
print(f"Second smallest is:{second_smallest}")