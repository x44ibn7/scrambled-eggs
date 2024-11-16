========
scrambled-eggs
========
This Python application allows you to encrypt and decrypt entire folders or individual files with a password. It uses Fernet encryption (from the cryptography library), a secure symmetric encryption algorithm. The app can handle single files, directories, and even recreate folder structures upon decryption.
You can either compile it yourself or download lastest release.
Releases have Input and Output folder located inside root/_internal folder.

========
Features
========
Encrypt a single file or entire folder: Place a file or folder in the Input directory, and the app will encrypt it into a single .enc file.

Decrypt files and folders: Decrypt encrypted files and restore original folder structures.

Password-based encryption: The encryption key is derived from the password you provide, ensuring only authorized access.

Folder compression: If a folder is provided, it is first compressed into a zip file before encryption, making it easy to process multiple files.


========
Prerequisites
========
Ensure you have the following Python packages installed:

---cryptography (for encryption)
---hashlib and base64 (for password-based key derivation)
---zipfile (for folder compression)

You can install the required package with:

>pip install cryptography

========
How to Use
========
1. Cipher (Encrypt) a File/Folder


---Place a file or folder in the Input directory.

---Run the script and choose Option 1 to encrypt.

---Enter a password when prompted.


The encrypted file(s) will be saved in the Output directory.

2. Decipher (Decrypt) a File/Folder
   
---Place the encrypted file(s) in the Input directory.

---Run the script and choose Option 2 to decrypt.

---Enter the password used during encryption.

The decrypted file(s) will be saved in the Output directory, and if it was a folder, the original folder structure will be restored.


========
How It Works
========
---Password-Based Key Derivation: The password you provide is used to generate a secure key using SHA-256 hashing, ensuring that only the correct password can decrypt the file.

---Encryption: Files and folders are encrypted using AES (Advanced Encryption Standard), which is a secure symmetric encryption algorithm.

---Decryption: The app uses the same password and key to decrypt the files, restoring them to their original form.

---Folder Compression: If a folder is encrypted, it is first compressed into a .zip file before encryption to preserve the folder structure.


========
File Structure
========
Input/: Folder where files or folders to be encrypted/decrypted should be placed.

Output/: Folder where encrypted/decrypted files are saved.

temp.zip: Temporary file used to store folder content before encryption. This file is removed after encryption and decryption.


========
Security Notes
========
---Password: Ensure you use a strong password to protect your files. The strength of the encryption depends on the complexity of the password.

---Key Management: The password you provide is used to derive the encryption key. If you forget the password, the files cannot be decrypted.

---Encryption Standard: The app uses Fernet encryption based on AES, which is considered secure and widely trusted.


========
License
========
This project is licensed under the MIT License - see the LICENSE file for details.
