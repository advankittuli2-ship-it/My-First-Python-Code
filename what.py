text = 'apple , mango , banana'
dirty_list = text.split(" , ")
clean_list = [word.strip() for word in dirty_list]
result = " and ".join(clean_list)

print(result)
print(clean_list)
