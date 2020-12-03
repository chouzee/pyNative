rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
el = []
for i in rollNumber:
    if i in sampleDict.values():
        el.append(i)
print("after removing unwanted elements from list ", el)
