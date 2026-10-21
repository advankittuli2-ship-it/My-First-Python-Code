d = {"a" : 1, "b" :2}
d["c"] = 3
d["a"] = d["a"] + 10
print(d["a"])
print(d)
print("b" in d)
print("z" in d)
d ["e"] = 30
del d ["a"]
del d ["b"]
print (d)