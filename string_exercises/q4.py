def lower_upper(str1):
    str1_lower = []
    str1_upper = []
    for str in str1:
        if str.islower():
            str1_lower.append(str)
        else:
            str1_upper.append(str)

    print(''.join(str1_lower + str1_upper))

str1 = "PyNaTive"
lower_upper(str1)