def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():  # Mengabaikan selain huruf
            shift = (ord(text[i].upper()) + ord(key[i].upper())) % 26
            encrypted_char = chr(shift + ord('A'))
            encrypted_text.append(encrypted_char if text[i].isupper() else encrypted_char.lower())
        else:
            encrypted_text.append(text[i])
    return "".join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key = generate_key(encrypted_text, key)
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():  # Mengabaikan selain huruf
            shift = (ord(encrypted_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            decrypted_text.append(decrypted_char if encrypted_text[i].isupper() else decrypted_char.lower())
        else:
            decrypted_text.append(encrypted_text[i])
    return "".join(decrypted_text)

# Input manual
text = input("Masukkan teks: ")
key = input("Masukkan kunci: ")

# Proses enkripsi
encrypted_text = vigenere_encrypt(text, key)
print("Teks terenkripsi:", encrypted_text)

# Proses dekripsi
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Teks terdekripsi:", decrypted_text)
