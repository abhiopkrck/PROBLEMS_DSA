set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common=set()
for num in set1:
    if num  in set2:
        common.add(num)
print(common)