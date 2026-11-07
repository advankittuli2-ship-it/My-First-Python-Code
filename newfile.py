text = "fir, judge, advocate"
dirty_list = text.split(" , ")
clean_list = [ ]
for word in dirty_list:
    clean_list.append(word.strip())
print(clean_list)

clean_list = [word.strip() for word in text.split(" , ")]
print(clean_list)
