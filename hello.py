first_name  = "manoj"
last_name = "sharma"

#old way without using formatted string
full_name = first_name + "" + last_name
#new way - now mosstly used way using formatted string
full_name = f"({first_name} {last_name})" 


full_name = f"Hello, {first_name} {last_name}!" 

print(full_name)

