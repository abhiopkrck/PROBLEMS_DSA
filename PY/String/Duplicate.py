text = "programming"

count={}

for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1

for char in text:
    if count[char]==2:
        print(char)
