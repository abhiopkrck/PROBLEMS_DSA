numbers = [10, 25, 7, 42, 18, 33, 20]

def even(numbers):
    count_even=0
    for num in numbers:
        if num%2==0:
            count_even+=1
    return count_even

even_total=even(numbers)
print("The total number of even numbers is:", even_total)