ramayana = ["Sita" , "  SITA", "sita", "RamSita" , "Shyam" , "ram"]

def count_name_in_list(names , target):
    count = 0
    for x in names:
        if x.lower().strip() == target.lower():
            count = count + 1
    return count
print(count_name_in_list(ramayana , "ram"))
print(count_name_in_list(ramayana , "sita"))
print(count_name_in_list(ramayana , "shyam"))