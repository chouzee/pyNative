n = 10
sum = 0
previous_num = 0
print("Printing current and previous number sum in a given range(10)")
for i in range(0, n+1, 1):
    sum = sum+i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {sum}")
    previous_num = i
