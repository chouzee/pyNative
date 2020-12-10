import random
import string


def generate_random_pass(length):
    letters = string.ascii_letters + string.digits
    passwd = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", passwd)
    
generate_random_pass(10)
