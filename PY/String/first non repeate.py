text = "programming"

count={}

first_non_repeat=None

for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in text:
    if count[char] ==1:
        print(char)
        break
for char in text:
    if count[char]==2:
        print(char)
        break