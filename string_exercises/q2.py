# s1 = "Ault"
# s2 = "Kelly"

# s1s = s1[:2]
# s1e = s1[-2:]
# print(s1s + s2 + s1e)


# output AuKellylt


def appending_middle_str(s1, s2):
    middle = int(len(s1) / 2)
    middle_string = s1[:middle:] + s2 + s1[middle:]
    print(middle_string)


s1 = "Ault"
s2 = "Kelly"
appending_middle_str(s1, s2)