numbers = [10, 20, 10, 30, 20, 40, 50]

count={}

for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num]=1

for num in numbers:
    if count[num]==1:
        print(num)
        break