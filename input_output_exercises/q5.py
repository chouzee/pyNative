user_input = int(input("Enter list size: "))

def return_list(user_input):
    float_list = []
    for i in range(0, user_input):
        items = float(input("Enter a numbers: "))
        float_list.append(items)
    return float_list
    
print(return_list(user_input))
