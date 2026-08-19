

def analyze(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    total=0
    for num in numbers:
        total+=num
    for num in numbers:
        if num>largest:
            largest=num
        elif num<smallest:
            smallest=num
    average=total/len(numbers)
    return largest,smallest,average

numbers = (12, 45, 23, 67, 34, 89, 10)

largest,smallest,average=analyze(numbers)

print(largest)
print(smallest)
print(average)