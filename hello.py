ramayana = ["sita" , "sIta" , "Ramsita" , "Shyam" , "rama"]

def count_between(names, low, high):
    count = 0
    for x in names:
        if low<= len(x.strip()) <= high:
            count = count + 1
    return count

print(count_between(ramayana, 1, 2))
print(count_between(ramayana, 2, 3))
print(count_between(ramayana, 3, 4))
print(count_between(ramayana, 4, 5))
print(count_between(ramayana, 5, 6))
print(count_between(ramayana, 6, 7))
print(count_between(ramayana, 7, 8))