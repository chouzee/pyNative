import secrets

generator = secrets.SystemRandom()
rand_digits = generator.randrange(100000, 999999)
print(rand_digits)
