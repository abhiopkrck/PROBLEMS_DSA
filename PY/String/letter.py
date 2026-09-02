text = "I love Python"

def count_word(text):
    count1=0
    count2=0
    for char in text:
        count1+=1
        if char ==" ":
            count2 +=1
            
    return count1-count2
        


  
count=count_word(text)     
print(count)