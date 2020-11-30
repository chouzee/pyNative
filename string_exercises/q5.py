def count(str1):
    lower_case = []
    upper_case = []
    digits = []
    special = []

    for l_c in str1:
        if l_c.islower():
            lower_case.append(l_c)
        elif l_c.isupper():
            upper_case.append(l_c)
        elif l_c.isdigit():
            digits.append(l_c)
        else:
            special.append(l_c)

    print("Lower case", len(lower_case))
    print("Upper case", len(upper_case))
    print("Digits", len(digits))
    print("Special chars", len(special))



str1 = "P@#yn26at^&i5ve"
count(str1)