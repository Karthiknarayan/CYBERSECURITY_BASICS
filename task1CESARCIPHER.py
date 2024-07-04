def caesar_encrypt(text, shift):
    """
    Encrypts the given text using the Caesar Cipher algorithm with the specified shift.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    """
    Decrypts the given text using the Caesar Cipher algorithm with the specified shift.
    """
    return caesar_encrypt(text, -shift)

def main():
    """
    Main function to run the Caesar Cipher program.
    """
    print("Caesar Cipher Program")
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'e':
            encrypted_message = caesar_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = caesar_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        
        again = input("Would you like to encrypt/decrypt another message? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
