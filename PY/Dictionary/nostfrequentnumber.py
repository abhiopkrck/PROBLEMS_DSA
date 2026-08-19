numbers = [1, 2, 2, 3, 11, 2, 4, 2]

count={}

for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num]=1


higest=0
mostcommon=None

for num in numbers:
    if count[num]>higest:
        higest=count[num]
        mostcommon=num

print(mostcommon)
print(higest)