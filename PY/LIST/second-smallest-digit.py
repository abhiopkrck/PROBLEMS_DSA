numbers=[12,23,34,45,56,67]

smallest=numbers[0]
second_smallest=numbers[0]

for num in numbers:
    if num<smallest:
        second_smallest=smallest
        smallest=num
    elif num<second_smallest:
        second_smallest=num

print(smallest)
print(second_smallest)