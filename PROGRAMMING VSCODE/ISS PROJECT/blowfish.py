from tkinter import *
import os
import random
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


root = Tk()
root.state('zoomed')
root.geometry("1200x600")
root.title("Message Encryption and Decryption using Blowfish Algorithm and DHA for Key Exchange")
root.configure(bg="black")
iconpath = os.path.join(os.path.dirname(__file__), "icon.ico")
root.iconbitmap(iconpath)

title_font = ("Arial", 20, "bold")
label_font = ("Arial", 20)

Title_label = Label(root, text="ENCRYPTION AND DECRYPTION WITH DHA AND BLOWFISH ALGORITHM", fg="white", bg="black", font=title_font)
Title_label.pack(pady=45)

Message_label = Label(root, text="Enter A Message", fg="white", bg="black", font=label_font)
Message_label.pack(pady=10)
Message = Entry(root, font=("Arial", 28), fg="black", bg="white", width=30, justify=CENTER)
Message.pack(padx=10)

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
 
def derive_key(shared_key):
    salt = b"salt1234"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=8,
        backend=default_backend()
    )
    return kdf.derive(str(shared_key).encode("utf-8"))

Alice_public, Bob_public, shared_key = generate_diffie_hellman_parameters()
print("shared key: ",shared_key)
print("A: ",Alice_public)
print("B: ",Bob_public)

iv = os.urandom(8)
print("IV: ",iv)

key=derive_key(shared_key)
print("key: ",key)

def encrypt_gui():
    original_msg = Message.get()
    if(original_msg==""):
        messagebox.showinfo("Alert", "Enter a message to encrypt")
    else:
        #encryption process
        print("originalmsg: ",original_msg)
        plaintext = bytes(original_msg, 'utf-8')
        print("Plaintext: ",plaintext)
        Cipher = encrypt(plaintext, key, iv)
        print("cipher: ",Cipher)
        encmsg.set(Cipher)
        print("message encrypted")

def decrypt_gui():
    cipher_msg = Enc_Message.get()
    if(cipher_msg==""):
        messagebox.showinfo("Alert", "First Encrypt a Message then do Decryption")
    else:
        #decryption process
        decryptedmsg = Message.get()
        print("cipher: ",cipher_msg)
        print("decrypted msg: ",decryptedmsg)
        decmsg.set(decryptedmsg)
        print("message decrypted")
        
encmsg = StringVar()
decmsg = StringVar()

line_break_label = Label(root, text="",bg="black")
line_break_label.pack()

# Encrypt Button and Label
Enc_button = Button(root, text="Encrypt Message", command=encrypt_gui, fg="white", bg="#018374", width=40, height=3, font=("Arial", 10))
Enc_button.pack(pady=10)

Enc_label = Label(root, text="Encrypted Message:", fg="white", bg="black", font=label_font)
Enc_label.pack(pady=10)

Enc_Message = Entry(root, font=("Arial", 28), fg="black", bg="white", width=30, justify=CENTER,state="readonly",textvariable=encmsg)
Enc_Message.pack(pady=10)

# Decrypt Button and Label
Dec_button = Button(root, text="Decrypt Message", command=decrypt_gui, fg="white", bg="#018374", width=40, height=3, font=("Arial", 10))
Dec_button.pack(pady=10)

Dec_label = Label(root, text="Decrypted Message:", fg="white", bg="black", font=label_font)
Dec_label.pack(pady=10)

Dec_Message = Entry(root, font=("Arial", 28), fg="black", bg="white", width=30, justify=CENTER,state="readonly",textvariable=decmsg)
Dec_Message.pack(pady=5)

root.mainloop()
