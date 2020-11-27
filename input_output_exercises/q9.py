import os
fpath = 'test.txt'
print(os.stat(fpath).st_size == 0)
