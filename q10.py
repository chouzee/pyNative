def new_list(f_list, s_list):
    new_list = []
    # odd list
    for i in f_list:
        if i & 1:
         new_list.append(i)
    # even list
    for i in s_list:
        if i % 2 == 0:
            new_list.append(i)
    
    print(new_list)


f_list = [10, 20, 23, 11, 17]
s_list = [13, 43, 24, 36, 12]

new_list(f_list, s_list)

# FROM SOLUTION SECTION
def mergeList(listOne, listTwo):
    print("First List ", listOne)
    print("Second List ", listTwo)
    thirdList = []
    
    for num in listOne:
        if (num % 2 != 0):
            thirdList.append(num)
    for num in listTwo:
        if (num % 2 == 0):
            thirdList.append(num)
    return thirdList

listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print("result List is", mergeList(listOne, listTwo))
