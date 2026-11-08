text = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
dirty_list = text.split(",")
clean_list = [word.strip() for word in dirty_list]
result = "".join(clean_list)

print(result)
print(clean_list)
