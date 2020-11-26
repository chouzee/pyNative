def list_char_compare(llist):
    if llist[0] == llist[-1]:
        return True
    else:
        return False


llist = [1, 3, 4, 5, 65, 1]
print(list_char_compare(llist))
