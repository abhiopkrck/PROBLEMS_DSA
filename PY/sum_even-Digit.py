from PY.adddigit import digit

n=int(input("Enter number:"))
sum=0
odd_sum=0
diffrence=0
while n!=0:
    digit=n%10
    if digit%2==0:
        sum=sum+digit
    else:
        odd_sum=odd_sum+digit
    n=n//10

diffrence=sum-odd_sum

print("Sum of Even number:",sum)
print("Sum of Odd number:",odd_sum)
print("Sum of Difference:",diffrence)