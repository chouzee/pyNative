def char_match(s1, s2):
    x = True
    for i in s1:
        if i in s2:
            continue
        else:
            x = False
    return x


s1 = "Yn"
s2 = "PYnative"
res = char_match(s1, s2)
print(res)

s1 = "Ynf"
s2 = "PYnative"
res = char_match(s1, s2)
print(res)