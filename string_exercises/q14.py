str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_lsit = list()
for i in str_list:
    if i:
        new_lsit.append(i)
print(new_lsit)


# From solution section
# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)