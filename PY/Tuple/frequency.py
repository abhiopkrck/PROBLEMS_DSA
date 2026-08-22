numbers = [1, 2, 2, 3, 1, 2, 4, 2]

count={}

for num in numbers:
    if num in count:
        count[num] +=1
    else:
        count[num]=1
   

print(count)