numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6]

seen=set()

for num in numbers:
    seen.add(num)

print(len(seen))