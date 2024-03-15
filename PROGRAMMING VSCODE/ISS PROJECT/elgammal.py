'''import random
from sympy import mod_inverse, isprime

def generate_elgamal_keys(p, g, private_key):
    public_key = pow(g, private_key, p)
    return public_key

def elgamal_encrypt(plain_text, p, g, public_key):
    if isinstance(plain_text, int):
        # Encrypting a number
        plain_text = str(plain_text)
        is_text = False
    else:
        # Encrypting text
        is_text = True

    # Choose a random ephemeral private key
    ephemeral_private_key = random.randint(2, p - 2)

    # Calculate ephemeral public key
    ephemeral_public_key = pow(g, ephemeral_private_key, p)

    # Calculate shared secret
    shared_secret = pow(public_key, ephemeral_private_key, p)

    # Encrypt the message
    cipher_text_1 = pow(g, ephemeral_private_key, p)
    cipher_text_2 = [(ord(char) if is_text else int(char)) * pow(shared_secret, 1, p) % p for char in plain_text]

    return cipher_text_1, cipher_text_2, is_text

def elgamal_decrypt(cipher_text_1, cipher_text_2, private_key, p, is_text):
    # Calculate shared secret
    shared_secret = pow(cipher_text_1, private_key, p)

    # Decrypt the message
    decrypted_values = [(cipher_text_2[i] * mod_inverse(shared_secret, p)) % p for i in range(len(cipher_text_2))]

    if is_text:
        decrypted_text = ''.join([chr(value) for value in decrypted_values])
    else:
        decrypted_text = ''.join([str(value) for value in decrypted_values])

    return decrypted_text

# Example usage
p = 23  # Example prime number, replace with a larger prime in practice
g = 5   # Example primitive root

# Generate private key for Party A
private_key_A = random.randint(2, p - 2)
public_key_A = generate_elgamal_keys(p, g, private_key_A)

# Generate private key for Party B
private_key_B = random.randint(2, p - 2)
public_key_B = generate_elgamal_keys(p, g, private_key_B)

# Exchange public keys securely (in a real-world scenario, this would be done securely)
shared_secret_A = pow(public_key_B, private_key_A, p)
shared_secret_B = pow(public_key_A, private_key_B, p)

# Encryption and Decryption using ElGamal for numbers
number_to_encrypt = int(input("Enter the number to encrypt: "))
cipher_text_1, cipher_text_2, is_text = elgamal_encrypt(number_to_encrypt, p, g, public_key_A)
decrypted_number = int(elgamal_decrypt(cipher_text_1, cipher_text_2, private_key_A, p, is_text))

print("\nOriginal Number:", number_to_encrypt)
print("Encrypted Number:", (cipher_text_1, cipher_text_2))
print("Decrypted Number:", decrypted_number)

# Encryption and Decryption using ElGamal for text
text_to_encrypt = str(input("Enter the Text to Encrypt: "))
cipher_text_1, cipher_text_2, is_text = elgamal_encrypt(text_to_encrypt, p, g, public_key_A)
decrypted_text = elgamal_decrypt(cipher_text_1, cipher_text_2, private_key_A, p, is_text)

print("\nOriginal Text:", text_to_encrypt)
print("Encrypted Text:", (cipher_text_1, cipher_text_2))
print("Decrypted Text:", decrypted_text)


from Crypto.Util.number import inverse
import sympy
import random
from binascii import hexlify, unhexlify

def shared_secret(g,x,p):
  # Shared Secret (h)
  h = pow(g,x,p)
  return h

def encrypt(m,r,g,p,h):
  c1 = pow(g,r,p)
  # Stolen from https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/PublicKey/ElGamal.py
  c2 = (m * pow(h, r, p) ) % p
  return c1,c2

def decrypt(x,c1,c2,p):
  s = pow(c1,x,p)
  dm = (c2 * inverse(s,p)) % p
  return dm

if __name__ == "__main__":
  input_message = input("Enter message to encrypt: ")
  inputbytes = str.encode(input_message)
  m = int(hexlify(inputbytes), 16)
  p = sympy.randprime(m*2, m*4)
  g = sympy.randprime(int(m/2), m)
  x = random.randint(int(m/2),m)
  r = random.randint(int(m/2),m)

  print("Bob's MESSAGE         : {}".format(input_message))
  print("MESSAGE as an int (M) : {}".format(m))
  print("Prime number (P)      : {}".format(p))
  print("Generator (G)         : {}".format(g))
  print("Alice private key (X) : {}".format(x))
  print("Bob's private key (R) : {}".format(r))

  h = shared_secret(g,x,p)
  print("Shared secret (H)     : {}".format(h))

  c1, c2 = encrypt(m,r,g,p,h)
  print("Encrypted Message (C1): {}".format(c1))
  print("Encrypted Message (C2): {}".format(c2))

  dm = decrypt(x,c1,c2,p)
  print("Decrypted Integer (dm): {}".format(dm))
  x = format(dm, 'x')
  print("Decrypted Hex (x)     : {}".format(x))
  message = unhexlify(x)
  print("Decrypted Message     : {}".format(message))
  
  '''
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD


message = "Hello!"

key = ElGamal.generate(1024, Random.new().read)

while 1:
    k = random.StrongRandom().randint(1, key.p - 1)

    if GCD(k, key.p - 1) == 1:
        break

h = key.encrypt(message, k)

d = key.decrypt(h)
print(d)