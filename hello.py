food_item = input("enter food item name:").strip().lower()


food_items_dict = {
    "burger" : 100, 
    "pizza" : 200, 
    "juice" : 50, 
    "golgappe" : 50}

def getprice(food_item):
    return food_items_dict.get(food_item, 0)
        

print(getprice(food_item))