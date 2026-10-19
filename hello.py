sita_list = ["Sita" , "sita" , "SITA" , "Sitaram" , "RamSita" , "Shyam" , "Ram"]

def count_sita_in_list (sita_list):
    count_sita = 0
    for x in sita_list:
        if "sita" in x.lower():
            count_sita = count_sita + 1
    return count_sita
result = count_sita_in_list(sita_list)
print(result)





 
