## Pixel Manipulation for Image Encryption

This Python-based tool performs basic image encryption and decryption using pixel manipulation techniques. The encryption process involves altering pixel values through mathematical operations, ensuring the pixel values stay within valid ranges (0-255). This project demonstrates how fundamental image processing can be combined with simple cryptography concepts to secure image data.

## How It Works

1. **Encryption**: 
   - The image is loaded using the Pillow library and converted into a NumPy array for pixel manipulation.
   - Each pixel’s RGB values are modified by adding a constant (e.g., 100) to each component, making the image unreadable.
   - The resulting encrypted image is saved in a specified output format.

2. **Decryption**: 
   - The encrypted image is read and processed using the reverse operation, subtracting the constant added during encryption.
   - The original image is restored and saved as the decrypted output.

## Features

- **Image Encryption**: Modifies pixel values to encrypt images.
- **Image Decryption**: Restores the original image from encrypted data.
- **Simple Algorithm**: Uses basic arithmetic operations to alter pixel data.
- **Libraries**: Powered by Pillow for image handling and NumPy for fast array processing.

## Example

- **Original Image**: An image you wish to encrypt.
- **Encrypted Image**: An altered version of the image with pixel values transformed.
- **Decrypted Image**: The restored version of the original image after decryption.

## Key Learnings

- Manipulating images using the Pillow library.
- Implementing reversible pixel transformations for encryption and decryption.
- Efficient image data processing with NumPy arrays.
- Practical application of basic cryptography concepts.

## Limitations

- This is a simple encryption method and should not be used for securing sensitive data.
- The encryption is not robust against advanced cryptographic attacks and is intended for educational purposes.

