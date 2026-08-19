n = int(input("Enter a number:"))

original = n

max_frequency = 0
most_frequent = 0

for target in range(10):

    n = original
    frequency = 0

    while n != 0:
        digit = n % 10

        if digit == target:
            frequency += 1

        n = n // 10

    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent = target

print("Most frequent digit:", most_frequent)
print("Frequency:", max_frequency)