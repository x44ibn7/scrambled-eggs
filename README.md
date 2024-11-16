scrambled-eggs

This Python application allows you to encrypt and decrypt entire folders or individual files with a password. It uses Fernet encryption (from the cryptography library), a secure symmetric encryption algorithm. The app can handle single files, directories, and even recreate folder structures upon decryption.

Features

Encrypt a single file or entire folder: Place a file or folder in the Input directory, and the app will encrypt it into a single .enc file.
Decrypt files and folders: Decrypt encrypted files and restore original folder structures.
Password-based encryption: The encryption key is derived from the password you provide, ensuring only authorized access.
Folder compression: If a folder is provided, it is first compressed into a zip file before encryption, making it easy to process multiple files.
Prerequisites

Ensure you have the following Python packages installed:

cryptography (for encryption)
hashlib and base64 (for password-based key derivation)
zipfile (for folder compression)
You can install the required package with:

pip install cryptography
How to Use

1. Cipher (Encrypt) a File/Folder
Place a file or folder in the Input directory.
Run the script and choose Option 1 to encrypt.
Enter a password when prompted.
The encrypted file(s) will be saved in the Output directory.
Example (Encrypt Folder):

If you place a folder named docs in the Input directory, it will be encrypted and saved as a .enc file in Output.
Example (Encrypt Single File):

If you place a file named test.txt in the Input directory, it will be encrypted and saved as test.txt.enc in Output.
2. Decipher (Decrypt) a File/Folder
Place the encrypted file(s) in the Input directory.
Run the script and choose Option 2 to decrypt.
Enter the password used during encryption.
The decrypted file(s) will be saved in the Output directory, and if it was a folder, the original folder structure will be restored.
Example (Decrypt Folder):

If you place an encrypted .enc file in the Input directory, the app will decrypt it and restore the original folder structure in Output.
Example (Decrypt Single File):

If you place an encrypted file like test.txt.enc in the Input directory, the app will decrypt it to the original test.txt file.
How It Works

Password-Based Key Derivation: The password you provide is used to generate a secure key using SHA-256 hashing, ensuring that only the correct password can decrypt the file.
Encryption: Files and folders are encrypted using AES (Advanced Encryption Standard), which is a secure symmetric encryption algorithm.
Decryption: The app uses the same password and key to decrypt the files, restoring them to their original form.
Folder Compression: If a folder is encrypted, it is first compressed into a .zip file before encryption to preserve the folder structure.
File Structure

Input/: Folder where files or folders to be encrypted/decrypted should be placed.
Output/: Folder where encrypted/decrypted files are saved.
temp.zip: Temporary file used to store folder content before encryption. This file is removed after encryption and decryption.
Security Notes

Password: Ensure you use a strong password to protect your files. The strength of the encryption depends on the complexity of the password.
Key Management: The password you provide is used to derive the encryption key. If you forget the password, the files cannot be decrypted.
Encryption Standard: The app uses Fernet encryption based on AES, which is considered secure and widely trusted.
License

This project is licensed under the MIT License - see the LICENSE file for details.
