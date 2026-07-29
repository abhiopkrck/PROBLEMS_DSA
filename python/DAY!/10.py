word="marsaam"

reversed=""

for i in range(len(word)):
    reversed=word[i]+reversed
    
if word==reversed:
    print("true")
else:
    print("false")
    
print(reversed)