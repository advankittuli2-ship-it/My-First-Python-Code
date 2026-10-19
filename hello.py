#count how many times each pet appears in the list?
pets = ["dog" , "Cat" , "dog" , "CAT" , "cat"]

def counts_pets(pets_list):
    '''Classic example of Python being case sensitive - Python counting same words 
    differently due to diffrent types of cases of same word'''
    counts = {}
    for x in pets_list:
        counts[x] = counts.get(x, 0) + 1
    return counts 

my_result = counts_pets(pets)
print(my_result) 