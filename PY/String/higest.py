text = "programming"

count={}


for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1

higest=0
highest_char=None

for char in text:
    if count[char]>higest:
        higest=count[char]
        highest_char=char

print(f"higest_char:{highest_char} \n Higest:{higest}")