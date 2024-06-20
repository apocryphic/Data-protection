def encrypt_scytale(message, key):
    message = message.replace(" ", "").lower()
    encrypted_message = [''] * key

    for i in range(len(message)):
        row = i % key
        encrypted_message[row] += message[i]

    return ''.join(encrypted_message)

def decrypt_scytale(encrypted_message, key):
    n = len(encrypted_message)
    decrypted_message = [''] * n
    num_cols = n // key
    extra_chars = n % key

    index = 0
    for col in range(num_cols):
        for row in range(key):
            decrypted_message[row * num_cols + col] = encrypted_message[index]
            index += 1

    for row in range(extra_chars):
        decrypted_message[(num_cols * key) + row] = encrypted_message[index]
        index += 1

    return ''.join(decrypted_message)

if __name__ == "__main__":
    message = input("Введіть повідомлення: ")
    key = int(input("Введіть ключ (кількість рядків): "))

    encrypted_message = encrypt_scytale(message, key)
    print(f"Зашифроване повідомлення: {encrypted_message}")

    decrypted_message = decrypt_scytale(encrypted_message, key)
    print(f"Розшифроване повідомлення: {decrypted_message}")
