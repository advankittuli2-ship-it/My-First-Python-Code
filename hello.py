ramayana = ["sita" , "sIta" , "Ramsita" , "Shyam" , "rama"]

def count_shorter(names, low, high):
    count = 0
    for x in names:
        if low<= len(x.strip()) <= high:
            count = count + 1
    return count

print(count_shorter(ramayana, 1, 2))
print(count_shorter(ramayana, 2, 3))
print(count_shorter(ramayana, 3, 4))
print(count_shorter(ramayana, 4, 5))
print(count_shorter(ramayana, 5, 6))
print(count_shorter(ramayana, 6, 7))
print(count_shorter(ramayana, 7, 8))