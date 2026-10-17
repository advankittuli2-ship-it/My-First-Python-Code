pets = ["dog" , "cat" , "monkey" , "cat" , "elephant"]
counts ={}

for x in pets:
    if x in counts:
        counts[x]  = counts[x] + 1
    else:
        counts[x] = 1
print(counts)

