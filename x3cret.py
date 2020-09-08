# designed by @mrturkishcoffee
# X3cret is a passwd generator packed with password meter and hashing capabilities

import string
import secrets
import random
import hashlib
from argon2 import PasswordHasher
from password_strength import PasswordPolicy, PasswordStats

randoms = string.ascii_letters + string.punctuation
random_number = random.randrange(100,999)
symbols = [ "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]",
            "^", "{", "|", "}", "~"]
random_string = ''.join(secrets.choice(randoms) for i in range(2))
random_symbol = ''.join(secrets.choice(symbols) for i in range(1))
random_symbol2 = ''.join(secrets.choice(string.punctuation) for i in range (1))

policy = PasswordPolicy.from_names(
    length=15,  # min length: 15
    uppercase=2,  # need min. 2 uppercase letters
    numbers=3,  # need min. 3 digits
    special=2,  # need min. 2 special characters
)

while True:
    na = input("Enter a word (min 5 chars)")
    if len(na) > 4:
        al = input("Enter a verb (min 5 chars)")
        if len(al) > 4:
            break

def slicing():
    name = na[0:4]
    alias = al[0:4]
    global full
    full = "".join(name.title()) + random_symbol + alias.title() + random_symbol2 + random_string + str(random_number)
    return
slicing()

print("This is your password ", full)
print("Your password is ", len(full), "chars long")
print("Let s improve the following:", policy.test(full))
stats = PasswordStats(full)
print("Here is the password strength:", stats.strength())

if stats.strength() > 0.66:
    print("Your password is strong")
else:
    print("Your password is weak, try more complex inputs")

hash_object = hashlib.md5(full.encode())
md5_hash = hash_object.hexdigest()
hash_object1 = hashlib.sha256(full.encode())
sha256 = hash_object1.hexdigest()
hash_object2 = PasswordHasher()
argon2 = hash_object2.hash(full)

if stats.strength() > 0.66:
    print("This is the MD5 hash of your password: ", md5_hash)
    print("This is the SHA256 hash of your password: ", sha256)
    print("This is the ARGON2id hash of your password: ", argon2)

