def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if character is alphabet
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if character is alphabet
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'b' to both encrypt and decrypt: ") 
    if choice.lower() == 'e':              #for encrypt
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Encrypted Text:", encrypted_text)
    elif choice.lower() == 'd':             #for decrypt
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print("Decrypted Text:", decrypted_text)
    elif choice.lower() == 'b':            #for encrypt and decrypt both
        text = input("Enter the text to encrypt and decrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher_encrypt(text, shift)
        decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
        print("Encrypted Text:", encrypted_text)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()