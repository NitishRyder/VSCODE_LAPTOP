import random
# Generate a random prime number P and a base number G.
P = random.randint(2**1024, 2**2048 - 1)
G = random.randint(2, P - 1)

# Alice generates her private key A and public key B.
A = random.randint(1, P - 1)
B = G**A % P

# Bob generates his private key B and public key A.
B = random.randint(1, P - 1)
A = G**B % P

# Alice and Bob exchange their public keys.

# Alice encrypts the message using ElGamal encryption.
def encrypt(message, P, G, A, B):
  # Generate a random integer K.
  K = random.randint(1, P - 1)

  # Calculate the ciphertext C1 and C2.
  C1 = G**K % P
  C2 = message * A**K % P

  # Return the ciphertext.
  return C1, C2

(C1, C2) = encrypt(message, P, G, A, B)

# Bob decrypts the message using ElGamal decryption.
def decrypt(ciphertext, P, G, A, B):
  # Calculate the plaintext.
  plaintext = ciphertext[1] * (B**ciphertext[0] % P)**-1 % P

  # Return the plaintext.
  return plaintext

plaintext = decrypt((C1, C2), P, G, A, B)

# Print the plaintext.
print(plaintext)

# Bob decrypts the message using ElGamal decryption.
def decrypt(ciphertext, P, G, A, B):
  # Calculate the plaintext.
  plaintext = ciphertext[1] * (B**ciphertext[0] % P)**-1 % P

  # Return the plaintext.
  return plaintext

plaintext = decrypt((C1, C2), P, G, A, B)

# Print the plaintext.
print(plaintext)