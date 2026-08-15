n=int(input("Enter a number:"))

even=0
odd=0
sum=0
while n!=0:
    digit=n%10
    if digit%2==0:
        even+=1
    elif digit%2!=0:
        odd+=1
    sum=sum+digit
    n=n//10

print("Even digits:",even)
print("Odd digits:",odd)
print("Sum of even and odd digits:",sum)