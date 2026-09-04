numbers = [10, 25, 7, 42, 18]

def find_largest(numbers):
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest

largest_number = find_largest(numbers)  
print("The largest number is:", largest_number)