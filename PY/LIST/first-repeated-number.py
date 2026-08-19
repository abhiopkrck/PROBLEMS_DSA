numbers = [10, 20, 30, 20, 40, 10]

seen=set()
foundfirst=None

for num in numbers:
    if num in seen:
        foundfirst=num
        break
    else:
        seen.add(num)
        
print(foundfirst)
print(seen)