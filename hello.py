ramayana = ["sita" , "sIta" ,"ramsita" , "shyam" , "ram" , "sita"]

def most_counts(names):
    count = {}
    for x in names:
        name = x.lower().strip()
        count[name] = count.get(name, 0) + 1
    return count
print(most_counts(ramayana))
        

