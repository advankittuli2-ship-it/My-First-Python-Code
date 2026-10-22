ramayana = ["sita" , "sIta" , "ramsita" , "shyam" , "ram ", "sita"]

def count_all(names):
    count = {}
    for x in names:
        name = x.lower().strip()
        if name in count:
            count[name] = count[name] + 1
        else:
            count[name] = 1
    return count

print(count_all(ramayana))
