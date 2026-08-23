text = "programming"

vowels=0
Consonants=0

for char in text:
    if char in "aeiou":
        vowels+=1
    else:
        Consonants+=1
        
print(f"Vowels:{vowels}")
print(f"Consonants:{Consonants}")