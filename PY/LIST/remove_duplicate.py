numbers=[1,2,2,1,3,4,4,3,5,5]

number=set()
unique=[]

for num in numbers:
    if num not in number:
        number.add(num)
        unique.append(num)

print(unique)
