import string

str1 = "/*Jon is @developer & musician"
trans = str1.translate(str.maketrans('','', string.punctuation))
print(trans)


#Another solution using regex
import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

str2 = re.sub(r'[^\w\s]', '', str1)
print("New string is ", str2)
