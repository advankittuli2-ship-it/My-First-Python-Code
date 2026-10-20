#for first time i have written a code only from memory and my own understanding ! Congrats to myself. 
sita_list = ["Sita" , "SITA", "sita", "RamSita" , "Shyam" , "Ram"]

def count_sita_in_list(sita_list):
    count_sita = 0
    for x in sita_list:
        if "sita" in x.lower().strip():
            count_sita = count_sita + 1
    return count_sita

result = count_sita_in_list(sita_list)
print(result)