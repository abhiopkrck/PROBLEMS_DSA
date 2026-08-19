number=[0,0,34,45,56,0,78,89]

result=[]
zero_count=0

for num in number:
    if num == 0:
        zero_count+=1
    else:
        result.append(num)
for i in range(zero_count):
    result.append(0)
print(zero_count)
print(result)


lists=[12,1,2,3,4,1,2,1,1]
one=0
result2=[]

for num in lists:
    if num ==1:
        one+=1
    else:
        result2.append(num)

for i in range(one):
    result.append(1)

print(result)