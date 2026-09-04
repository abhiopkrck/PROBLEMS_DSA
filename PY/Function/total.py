numbers = [10, 25, 7, 42, 18]

def total(numbers):
    total=0
    for num in numbers:
        total+=num
    return total

total_list=total(numbers)
print(total_list)