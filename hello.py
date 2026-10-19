#count how many times each pet appears in the list?
pets = ["dog " , "Dog" , "DOG" , "cat" , "CAT"]

def counts_pets(pets_list):
    counts = {}
    for x in pets_list:
        lower_x = x.lower().strip()
        counts[lower_x] = counts.get(lower_x, 0) + 1
    return counts

my_result = counts_pets(pets)
print(my_result)

