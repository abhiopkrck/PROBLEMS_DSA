numbers=[1,2,3,4,5,8,9,10]

total=0
actual=0

for i in range(1,11):
    total+=i
for num in numbers:
    actual+=num


print(actual)
print(total)
print(total-actual)