numbers = [10, 25, 7, 42, 18, 33, 20]

def odd_total(numbers):
    total=0
    for num in numbers:
        if num%2!=0:
            total+=num
    return total
odd_totala=odd_total(numbers)
print("The total number of odd numbers is:", odd_totala)