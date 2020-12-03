f = {65, 42, 78, 83, 23, 57, 29}
s = {67, 73, 43, 48, 83, 57, 29}

diff = f.intersection(s)
print("Intersection is ", diff)
for i in diff:
    f.remove(i)
print("First set after removing common element ", f)
