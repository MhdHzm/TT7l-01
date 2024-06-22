from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypting data
plain_text = b"Sensitive user data"
cipher_text = cipher_suite.encrypt(plain_text)

# Decrypting data
decrypted_text = cipher_suite.decrypt(cipher_text)
print(decrypted_text.decode())