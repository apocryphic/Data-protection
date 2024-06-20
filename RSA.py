import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    
    p = 13
    q = 11
    
    print("Генерація ключів RSA...")
    public, private = generate_keypair(p, q)
    print("Публічний ключ:", public)
    print("Приватний ключ:", private)
    
    
    message = input("Введіть повідомлення для шифрування: ")
    
    
    encrypted_msg = encrypt(public, message)
    print("Зашифроване повідомлення:", encrypted_msg)
    
    
    with open("message.txt", "w", encoding="utf-8") as file:
        file.write(message)
    
    with open("encrypted_message.txt", "w", encoding="utf-8") as file:
        file.write(' '.join(map(str, encrypted_msg)))
    
   
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Розшифроване повідомлення:", decrypted_msg)
    
    
    with open("decrypted_message.txt", "w", encoding="utf-8") as file:
        file.write(decrypted_msg)
