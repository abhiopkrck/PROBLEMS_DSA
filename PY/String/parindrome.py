
def is_palindrome(text):
    revers=""
    for char in text:
        revers=char+revers
    if revers==text:
        return True
    else:
        return False

result = is_palindrome("madam")
print(result)