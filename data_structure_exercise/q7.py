firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}

first_sub = firstSet.issubset(secondSet)
second_sub = secondSet.issubset(firstSet)

print("First set is subset of second set - ", first_sub)
print("Second set is subset of First set - ", second_sub)

first_super_sub = firstSet.issuperset(secondSet)
second_super_sub = secondSet.issuperset(firstSet)
print("First set is Super set of second set ", first_super_sub)
print("Second set is Super set of First set ", second_super_sub)

print("First Set ", firstSet)
print("Second Set ", secondSet)
