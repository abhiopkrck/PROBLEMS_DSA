text="Python"

reverse=text[::-1]

print(reverse)

reverse_2="".join(reversed(text))

print(reverse_2)

reverse_3=""

for char in text:
    reverse_3=char+reverse_3

print(reverse_3)