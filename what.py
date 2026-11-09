satish = "+9101254820.html"
nigam  = "+912639341.html"
pardeep = "+9112548211.html"
mobile_directory = [satish , nigam , pardeep]
new_mobile_directory = [numbers.removeprefix("+91").removesuffix(".html") for numbers in mobile_directory]
print(new_mobile_directory)