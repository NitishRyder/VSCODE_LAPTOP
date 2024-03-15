import random
from sympy import mod_inverse, isprime

# Diffie-Hellman Key Exchange
def generate_dh_parameters():
    # Select large prime number and its primitive root
    p = 23  # Example prime number, replace with a larger prime in practice
    g = 5   # Example primitive root

    # Choose private keys for both parties
    private_key_A = random.randint(2, p - 2)
    private_key_B = random.randint(2, p - 2)

    # Calculate public keys
    public_key_A = pow(g, private_key_A, p)
    public_key_B = pow(g, private_key_B, p)

    # Calculate shared secret
    shared_secret_A = pow(public_key_B, private_key_A, p)
    shared_secret_B = pow(public_key_A, private_key_B, p)

    return p, g, public_key_A, public_key_B, shared_secret_A, shared_secret_B

# ElGamal Encryption and Decryption
def generate_elgamal_keys(p, g, private_key):
    # Calculate public key
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

# Main program
print("DIFFE HELLMAN KEY EXCHANGE")
p, g, public_key_A, public_key_B, shared_secret_A, shared_secret_B = generate_dh_parameters()
print("Public Key A:", public_key_A)
print("Public Key B:", public_key_B)
print("Shared Secret A:", shared_secret_A)
print("Shared Secret B:", shared_secret_B)

# Get user input (text or number)
user_input = input("\nEnter text or number to encrypt: ")

# Party A
private_key_A = random.randint(2, p - 2)
public_key_A = generate_elgamal_keys(p, g, private_key_A)

# Party B
private_key_B = random.randint(2, p - 2)
public_key_B = generate_elgamal_keys(p, g, private_key_B)

# Exchange public keys securely (in a real-world scenario, this would be done securely)
shared_secret_A = pow(public_key_B, private_key_A, p)
shared_secret_B = pow(public_key_A, private_key_B, p)

# Encryption and Decryption using ElGamal
cipher_text_1, cipher_text_2, is_text = elgamal_encrypt(user_input, p, g, public_key_A)
decrypted_text = elgamal_decrypt(cipher_text_1, cipher_text_2, private_key_A, p, is_text)

# Display results
print("\nOriginal Input:", user_input)
print("Encrypted Message:", (cipher_text_1, cipher_text_2))
print("Decrypted Message:", decrypted_text)
