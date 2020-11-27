def extract_reverse_order(values):
    
    while values > 0:
        digit = values % 10
        values = values // 10
        print(digit, end= " ")

extract_reverse_order(7536)
