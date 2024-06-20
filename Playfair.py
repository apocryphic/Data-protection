def generate_key_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper().replace('J', 'I')
    key_matrix = []

  
    for char in keyword:
        if char not in key_matrix:
            key_matrix.append(char)

   
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(key_matrix, char):
    for i, row in enumerate(key_matrix):
        for j, matrix_char in enumerate(row):
            if matrix_char == char:
                return i, j

def playfair_encrypt(plaintext, keyword):
    key_matrix = generate_key_matrix(keyword)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    
    
    i = 0
    while i < len(plaintext):
        if i+1 < len(plaintext) and plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + 'X' + plaintext[i+1:]
        i += 2

    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, keyword):
    key_matrix = generate_key_matrix(keyword)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]

    
    plaintext = plaintext.replace('X', '')
    
    return plaintext

if __name__ == "__main__":
    keyword = input("Введіть гасло: ")
    plaintext = input("Введіть повідомлення: ")
    
    ciphertext = playfair_encrypt(plaintext, keyword)
    print(f"Шифрограма: {ciphertext}")
    
    decrypted_text = playfair_decrypt(ciphertext, keyword)
    print(f"Розшифроване повідомлення: {decrypted_text}")
