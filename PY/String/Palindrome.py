text = "noden"
reverse=""

for char in text :
    reverse=char+reverse

print(reverse)


if text==reverse:
    print("True")
else:
    print("False")
    