original = [34, 54, 67, 89, 11, 43, 94]
print("Original list", original)

original.remove(11)
print("List After removing element at index 4", original)

original[2] = 11
print("List after Adding element at index 2", original)

original[-1] = 11
print("List after Adding element at last", original)

# here is from solution section
sampleList = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)

sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)

sampleList.append(element)
print("List after Adding element at last ", sampleList)