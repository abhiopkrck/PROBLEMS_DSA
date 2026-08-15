n=int(input("Enter a number:"))
target=int(input("Enter a target number:"))
same=0

while n!=0:
    digit=n%10
    if digit==target:
        same+=1
    n=n//10
    
print(f"The number of times {target} appears in the number is:",same)