ram_list = ["Ram" , "RAM" , "ram" , "ayaram" , "gayaram" , "heyram" , "kuonram", "goram"]

def count_ram_in_list(my_list):
    count_ram = 0
    for x in my_list:
        if "ram" in x.lower():
            count_ram = count_ram + 1
    return count_ram
result = count_ram_in_list(ram_list)
print(result)





 
