def return_three_chars(s1, s2):
    length_s1 = int(len(s1) / 2)
    length_s2 = int(len(s2) / 2)
    new_string = s1[0] + s2[0] + s1[length_s1] + s2[length_s2] + s1[-1] + s2[-1]
    print(new_string)
    


s1 = "America"
s2 = "Japan"
return_three_chars(s1, s2)