number=[12,23,34,45,56,67,78]

total=0
nums=set()
greatest_count=0

for num in number:
    total+=num

average=total/len(number)
for num in number:
    if num>average:
        greatest_count+=1

print(average)
print(greatest_count)
print()