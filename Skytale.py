def encrypt_scytale(message, key):
    
    encrypted_text = [''] * key
    for i, char in enumerate(message):
        encrypted_text[i % key] += char
    return ''.join(encrypted_text)

def decrypt_scytale(encrypted_text, key):

    decrypted_text = [''] * len(encrypted_text)
    rows = len(encrypted_text) // key
    cols = key
    
   
    index = 0
    for col in range(cols):
        for row in range(rows):
            decrypted_text[row * cols + col] = encrypted_text[index]
            index += 1
    
 
    return ''.join(decrypted_text)

def main():
    choice = input("Виберіть операцію:\n1. Шифрування\n2. Розшифрування\n")
    
    if choice == '1':
        message = input("Введіть повідомлення для шифрування: ")
        key = int(input("Введіть ключ (ширина Сцітали): "))
        
    
        encrypted_text = encrypt_scytale(message, key)
        print("Зашифроване повідомлення: ", encrypted_text)
        
    elif choice == '2':
        encrypted_text = input("Введіть зашифроване повідомлення: ")
        key = int(input("Введіть ключ (ширина Сцітали): "))
        
 
        decrypted_text = decrypt_scytale(encrypted_text, key)
        print("Розшифроване повідомлення: ", decrypted_text)
        
    else:
        print("Невірний вибір операції. Будь ласка, виберіть 1 або 2.")

if __name__ == "__main__":
    main()
