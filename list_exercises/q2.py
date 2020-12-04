list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]

zipped = []
for i, j in zip(list1, list2):
    zipped.append(i+j)
print(zipped)
