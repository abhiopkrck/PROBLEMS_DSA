set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

not_in_set2=set()

for num in set1:
    if num not in set2:
        not_in_set2.add(num)
print(not_in_set2)