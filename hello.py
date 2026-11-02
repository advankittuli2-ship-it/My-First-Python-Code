name1 = "Ram"
name2 = "RAM"
name3 = " ram "
print(name1 == name2)
print(name1.lower() ==name2.lower())
clean_name3 = name3.strip().lower()
print(clean_name3 == name1.lower())