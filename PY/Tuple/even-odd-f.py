numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
result={
    "even":{},
    "odd":{}
}

for num in numbers:
    if num%2==0:
        if num in result["even"]:
            result["even"][num]+=1
    else:
        result["even"][num]=1
    
    if num in result["odd"]:
        result["odd"][num]+=1
    else:
        result["odd"][num]=1

print(result)