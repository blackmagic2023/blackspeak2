from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(message, key):
    key_obj = RSA.import_key(key)
    cipher_rsa = PKCS1_OAEP.new(key_obj)
    session_key = get_random_bytes(16)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())
    encrypted_session_key = cipher_rsa.encrypt(session_key)
    return encrypted_session_key, cipher_aes.nonce, tag, ciphertext

def decrypt_message(encrypted_session_key, nonce, tag, ciphertext, private_key):
    key_obj = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(key_obj)
    session_key = cipher_rsa.decrypt(encrypted_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
    decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return decrypted_message.decode()

def main():
    private_key, public_key = generate_key_pair()

    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted_session_key, nonce, tag, ciphertext = encrypt_message(message, public_key)
            print("Encrypted message:", base64.b64encode(encrypted_session_key).decode(), base64.b64encode(nonce).decode(), base64.b64encode(tag).decode(), base64.b64encode(ciphertext).decode())

        elif choice == '2':
            encrypted_session_key = base64.b64decode(input("Enter the encrypted session key: "))
            nonce = base64.b64decode(input("Enter the nonce: "))
            tag = base64.b64decode(input("Enter the tag: "))
            ciphertext = base64.b64decode(input("Enter the ciphertext: "))
            message = decrypt_message(encrypted_session_key, nonce, tag, ciphertext, private_key)
            print("Decrypted message:", message)

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
