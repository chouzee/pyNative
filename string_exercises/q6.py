def mixed_string(s1, s2):
    middle_s1 = int(len(s1) /2)
    middle_s2 = int(len(s2) /2)
    mixed_string = s1[0] + s2[-1] + s1[middle_s1] + s2[middle_s2] + s1[-1] + s2[0]
    print(mixed_string)



s1 = "Abc"
s2 = "Xyz"
mixed_string(s1, s2)