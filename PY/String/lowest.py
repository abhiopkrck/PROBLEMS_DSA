text = "programming"

count={}


for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1

lowest=float("inf")
lowest_char=None

for char in text:
    if count[char]<lowest:
        lowest=count[char]
        lowest_char=char

print(f"higest_char:{lowest_char} \n Higest:{lowest}")