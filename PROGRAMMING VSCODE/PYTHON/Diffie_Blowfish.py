'''
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
 
# Diffie-Hellman Key Exchange
def generate_diffie_hellman_parameters():
    prime = 23  # A small prime number for demonstration purposes
    alpha = 5   # A primitive root modulo prime
 
    # Alice generates her private key (a)
    a_private_key = random.randint(1, prime - 1)
    A = pow(alpha, a_private_key, prime)
 
    # Bob generates his private key (b)
    b_private_key = random.randint(1, prime - 1)
    B = pow(alpha, b_private_key, prime)
 
    # Shared secret key
    shared_secret_key = pow(B, a_private_key, prime)
 
    return A, B, shared_secret_key
 
# Blowfish Encryption and Decryption
def encrypt(text, key, iv):
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text) + encryptor.finalize()
    return ciphertext
 
def decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_text
 
# Example usage
if __name__ == "__main__":
    # Diffie-Hellman key exchange
    Alice_public, Bob_public, shared_key = generate_diffie_hellman_parameters()
   
    # Messages to be encrypted
    x = "Hi I am Nitish"
    plaintext = b"x"
 
    # Derive a key from the shared secret using PBKDF2
    salt = b"ABCD1234"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=8,
        backend=default_backend()
    )
    key = kdf.derive(str(shared_key).encode("utf-8"))
 
    # Generate a random IV
    iv = os.urandom(8)  # Use an appropriate IV size for your encryption algorithm
 
    # Encrypt using Blowfish
    ciphertext = encrypt(plaintext, key, iv)
 
    # Decrypt using Blowfish
    decrypted_text = decrypt(ciphertext, key, iv)
 
    print("Original Text:", plaintext)
    print("Encrypted Text:", ciphertext)
    print("Decrypted Text:", decrypted_text.decode("utf-8"))
'''
import base64
from Crypto.Cipher import Blowfish
from Crypto.Protocol.KDF import HKDF
from Crypto.Random import get_random_bytes
from pyDH import DiffieHellman

# Step 1: Set up the keys
alice = DiffieHellman()
bob = DiffieHellman()

# Step 2: Generate public keys for each person
alice_public = alice.gen_public_key()
bob_public = bob.gen_public_key()

# Step 3: Exchange public keys and calculate the shared secret key
alice_shared_secret = alice.compute_shared_secret(bob_public)
bob_shared_secret = bob.compute_shared_secret(alice_public)

# Check if both keys are equal
assert alice_shared_secret == bob_shared_secret

# Step 4: Encrypt and decrypt messages using the shared secret key
message = "This is a test message for encryption and decryption"

# Create a key and IV for Blowfish algorithm using HKDF
key = HKDF(alice_shared_secret, 32, b'', b'', hashmod =hashlib.sha256).hexread(32)
iv = get_random_bytes(8)

# Encrypt the message using Blowfish algorithm
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
ciphertext = base64.b64encode(iv + cipher.encrypt(message))

# Decrypt the message using Blowfish algorithm
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plaintext = cipher.decrypt(base64.b64decode(ciphertext)[8:])

print(f"Encrypted message: {ciphertext}")
print(f"Decrypted message: {plaintext}")