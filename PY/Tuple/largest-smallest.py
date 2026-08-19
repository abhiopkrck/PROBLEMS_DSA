numbers = (12, 23, 34, 45, 56, 67)

smallest=numbers[0]
largest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
print(smallest)
print(largest)