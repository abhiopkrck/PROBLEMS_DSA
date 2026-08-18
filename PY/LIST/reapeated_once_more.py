numbers=[12,12,23,34,23,65]

repeated_store=set()
repeated=[]
for num in numbers:
    if num in repeated_store:
        repeated.append(num)
    else:
        repeated_store.add(num)

print(repeated)