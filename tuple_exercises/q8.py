tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

sorted_tuple = sorted(tuple1, key=lambda tup: tup[1])
print(sorted_tuple)
