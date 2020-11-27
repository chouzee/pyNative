def reverse_number(number):
    print(f"Original number is {number}")
    if str(number) == str(number)[::-1]:
        print("The original and reverse number is the same")
    else:
        print("The original and reverse number is not the same")
        
reverse_number(121)
