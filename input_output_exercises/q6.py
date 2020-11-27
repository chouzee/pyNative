with open('test.txt', 'r') as f:
    with open('test1.txt', 'w') as f1:
        lines = f.readlines()
        count = len(lines)
        for line in lines:
            if count == 3:
                count -= 1
                continue
            else:
                f1.write(line)
            count -= 1
