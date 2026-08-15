n=int(input("Enter a number:"))
count=0

seen=set()

count=0

while n!=0:
    digit=n%10
    if digit in seen:
        print(f"{digit} is repeated")
    else:
        print(f"{digit} mot repeated")
        count+=1
        seen.add(digit)
    n=n//10

print(count)