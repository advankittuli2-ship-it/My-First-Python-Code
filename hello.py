food_item = input("enter food item name:")

def getprice(food_item):
    if food_item == "burger":
        return 250
    elif food_item == "pizza":
        return 550
    elif food_item == "juice":
        return 10
        

print(getprice(food_item))