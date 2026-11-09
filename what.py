satish = "+9101254820"
nigam  = "+912639341"
pardeep = "+9112548211"
mobile_directory = [satish , nigam , pardeep]
clean_numbers = [ ]
for number in mobile_directory:
    clean_number = number.removeprefix("+91")
    clean_numbers.append(clean_number)

print(clean_numbers)


