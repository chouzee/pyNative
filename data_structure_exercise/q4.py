s_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
item_count = {}

for key in s_list:
    if key in item_count:
        item_count[key] += 1
    else:
        item_count[key] = 1
print("Printing count of each item", item_count)
