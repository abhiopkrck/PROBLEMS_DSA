numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

seen=set()

for num in numbers:
    if num not in seen:
        seen.add(num)
    else:
        print(num)