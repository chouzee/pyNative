def largest_item(alist):
    alist.sort()
    return alist[-1]


alist = [4, 6, 8, 24, 12, 2]
res = largest_item(alist)
print(res)
