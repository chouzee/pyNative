import secrets

# generate a secure 64b token
bit_number = secrets.token_hex(64)

url_part = "example.com/v1/214/reset/"
rand_url = url_part + secrets.token_urlsafe(32)
print("Random 64 bit token is: ", bit_number)
print("Random url is: ", rand_url)
