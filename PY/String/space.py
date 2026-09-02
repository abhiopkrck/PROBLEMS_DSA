text = "I am learning Python"
def count_word(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count+1

count=count_word(text)

print(count)