numbers=[12,23,34,45,56,67]

largest=numbers[0]
second_largest=numbers[0]

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest:
        second_largest=num

print(f"Larggest first:{largest}")
print(f"Second largest:{second_largest}")