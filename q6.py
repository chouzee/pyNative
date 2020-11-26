def return_divisible(my_list):
    print("The original list is", my_list)
    print("Divisible of 5 in a list")
    for i in my_list:
        if i % 5 == 0:
            print(i)
            
my_list = [10, 20, 33, 46, 55]            
return_divisible(my_list)
