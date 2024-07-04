from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.int32)
    
    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    
    # Save the encrypted image
    if not any(output_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']):
        raise ValueError("Output path must end with a valid image extension (e.g., .png, .jpg, .jpeg, .bmp, .gif)")
    
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.int32)
    
    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    
    # Save the decrypted image
    if not any(output_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']):
        raise ValueError("Output path must end with a valid image extension (e.g., .png, .jpg, .jpeg, .bmp, .gif)")
    
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Image Encryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ")
    if choice.lower() not in ['e', 'd']:
        print("Invalid choice! Please choose 'e' for encrypt or 'd' for decrypt.")
        return
    
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the path for the output image (include a valid image extension, e.g., .png): ")
    key = int(input("Enter the encryption key (integer value): "))
    
    if choice.lower() == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice.lower() == 'd':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
    #simply to check