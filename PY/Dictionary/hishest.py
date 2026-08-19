numbers = [1, 2, 2, 3, 1, 2, 4, 2]

repeated=0
seen=set()

most_repeated=None
for num in numbers:
    if num in seen:
        repeated+=1
        most_repeated=num
    else:
        seen.add(num)

print(most_repeated)
print(repeated)
print(seen)