# Kat Hoadley - RSA Project
import random
import sympy
from sympy import isprime
import math

digits = 200
original_message = "Here is the secret message"
message_size = len(original_message)
message_bytes = original_message.encode('ascii')
message_int = int.from_bytes(message_bytes, byteorder='big')

def primeNumberGenerator (num_digits):
    min_val = 10 ** (num_digits - 1)
    max_val = (10 ** num_digits) - 1
    random_num = random.randint(min_val, max_val)

    while not isprime(random_num):
        random_num = random.randint(min_val, max_val)

    return random_num

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# key generator loop
e = 65537

while True:
    p = primeNumberGenerator(digits)
    q = primeNumberGenerator(digits)
    n = p * q
    phi_n = (p-1) * (q-1)

    if math.gcd(e, phi_n) == 1:
        break
    else:
        print("ERROR: e and phi(n) are not co-prime!")

(one, d, _) = gcd_extended(int(e), int(phi_n))

if one != 1:
    print("ERROR: e and phi(n) are not co-prime!")

d = (d + phi_n) % phi_n

print(f"pub key: ({n}, {e})")
print(f"priv key: ({n}, {d})")

encrypted_message = pow(message_int, e, n)
print("Encrypted message: ", encrypted_message)

decoded_int = pow(encrypted_message, d, n)

decoded_b = decoded_int.to_bytes(message_size, byteorder="big")
decoded_message = decoded_b.decode("ascii")

print("Decrypted message: ", decoded_message)