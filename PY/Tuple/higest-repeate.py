numbers = [1, 2, 2, 3, 1, 2, 4, 2]

count={}

for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num]=1

highest = 0
most_repeated = None

for num,frequency in count.items():
    if frequency>highest:
        highest=frequency
        most_repeated=num

print(count)
print(highest)
print(most_repeated)