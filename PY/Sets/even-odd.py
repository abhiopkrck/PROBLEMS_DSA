numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even=set()
odd=set()

for num in numbers:
    if num%2==0:
        even.add(num)
    else:
        odd.add(num)
print(even)
print(odd)