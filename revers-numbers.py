n=int(input("Enter number:"))

reverse=0

orignal=n

while n!=0: 
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
    
if reverse==orignal:  
    print("same")
    print(reverse)
else:
    print("not same")
    print(reverse)