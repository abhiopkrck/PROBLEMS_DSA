numbers=[12,23,34,45,56,67,78,89]

even=0
odd=0
sum_even=0
sum_odd=0

for num in numbers:
    if num%2==0:
        even+=1
        sum_even=num+sum_even
    elif num%2!=0:
        odd+=1
        sum_odd=num+sum_odd



print(f"Even numbers:{even}")
print(f"Odd numbers:{odd}")
print(f"Sum of even numbers:{sum_even}")
print(f"Sum of odd numbers:{sum_odd}")