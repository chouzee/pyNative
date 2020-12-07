def check(sampleTuple):
    return all(i == sampleTuple[0] for i in sampleTuple)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))
