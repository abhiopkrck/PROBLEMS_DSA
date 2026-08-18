numbers=[12,23,34,45,56,67]

largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
print(largest)
print(smallest)