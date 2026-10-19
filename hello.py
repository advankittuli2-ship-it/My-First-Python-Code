pets_list = ["dog" , "DOG" , "cat" , "CAT"]

def counts_pets(pets_list):
    counts = {}
    for x in pets_list:
        lower_x = x.lower(). strip()
        counts[lower_x] = counts.get(lower_x, 0) +1
    return counts
my_result = counts_pets(pets_list)
print(my_result) 