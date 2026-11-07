text = "fir, judge, advocate"
dirty_list = text.split(",")
clean_list = [word.strip() for word in dirty_list]
result = " and ".join(clean_list)

print(clean_list)
print(result)
