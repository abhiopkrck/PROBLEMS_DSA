numbers = [234, 25, 171, 412, 118]

def find_smallest(numbers):
    smallest=numbers[0]
    for num in numbers:
        if num<smallest:
            smallest=num
    return smallest

smallest_number=find_smallest(numbers)
print("The smallest number is:", smallest_number)