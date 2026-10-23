#append - adding your count to file
count = {"sita : 3" , "ram: 1"}

with open("ramayana.txt" , "a") as file:
    file.write(str(count))