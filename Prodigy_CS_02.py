import numpy as np
from PIL import Image

def encrypt_image(image_path, key, output_path):
    # Open the image and convert it to a NumPy array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Ensure the key is an integer
    key = int(key)

    # Encrypt the image by shifting pixel values
    encrypted_array = img_array + key
    encrypted_array = np.clip(encrypted_array, 0, 255)  

    # Save the encrypted image
    encrypted_img = Image.fromarray(np.uint8(encrypted_array))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")


def decrypt_image(image_path, key, output_path):
    # Open the encrypted image and convert it to a NumPy array
    img = Image.open(image_path)
    encrypted_array = np.array(img)

    key = int(key)

    # Decrypt the image by reversing the shift
    decrypted_array = encrypted_array - key
    decrypted_array = np.clip(decrypted_array, 0, 255)  
    # Save the decrypted image
    decrypted_img = Image.fromarray(np.uint8(decrypted_array))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")


if __name__ == "__main__":
    image_path = 'image.jpg'        
    encrypted_image_path = 'encrypted_image.png' 
    decrypted_image_path = 'decrypted_image.png'  
    key = 50  
    encrypt_image(image_path, key, encrypted_image_path)
    decrypt_image(encrypted_image_path, key, decrypted_image_path)
