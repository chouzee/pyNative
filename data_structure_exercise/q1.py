listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
third_list = []

first = listOne[1::2]
second = listTwo[0::2]
third_list.extend(first)
third_list.extend(second)
print("Element at odd-index positions from list one")
print(first)

print("Element at even-index positions from list two")
print(second)

print("Printing Final third list")
print(third_list)