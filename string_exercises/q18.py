from string import punctuation

char = '#'
str1 = '/*Jon is @developer & musician!!'
for i in punctuation:
    str1 = str1.replace(i, char)
print(str1)