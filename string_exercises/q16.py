str1 = "I am 25 years and 10 months old"
loop_res = [i for i in str1 if i.isdigit()]
res = ''.join(loop_res)
print(res)