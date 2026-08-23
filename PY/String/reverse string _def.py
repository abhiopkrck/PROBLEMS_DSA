text = "python"

def reverse_string(text):
    reverse=""
    for char in text:
        reverse=char+reverse
    return reverse

reverse=reverse_string(text)
print(reverse)