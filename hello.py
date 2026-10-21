ramayana = ["sita" , "sIta" , "Ramsita" , "Shyam" , "rama"]

def count_longer(names, size):
    count = 0
    for x in names:
        if len(x.strip())>size:
            count = count + 1
    return count

print(count_longer(ramayana, 5))
print(count_longer(ramayana, 3))
print(count_longer(ramayana, 2))
print(count_longer(ramayana, 4))
print(count_longer(ramayana, 1))
