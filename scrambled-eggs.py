import os
import hashlib
import base64
import shutil
import zipfile
from cryptography.fernet import Fernet

INPUT_DIR = "Input"
OUTPUT_DIR = "Output"
TEMP_ARCHIVE = "temp.zip"

def derive_key_from_password(password: str) -> bytes:
    """
    Derives a deterministic 32-byte key from a password.
    """
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def create_zip(folder_path: str, zip_path: str):
    """
    Compresses a folder into a zip file.
    """
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def extract_zip(zip_path: str, extract_to: str):
    """
    Extracts a zip file to a specified directory.
    """
    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(extract_to)

def cipher_folder_or_file():
    """
    Compresses and encrypts a folder or single file from INPUT_DIR to OUTPUT_DIR.
    """
    password = input("Enter the key: ")
    key = derive_key_from_password(password)
    fernet = Fernet(key)

    input_items = os.listdir(INPUT_DIR)
    if not input_items:
        print("Input folder is empty.")
        return

    # Handle single file or multiple files/folders
    if len(input_items) == 1 and os.path.isfile(os.path.join(INPUT_DIR, input_items[0])):
        # Single file in Input folder
        single_file_path = os.path.join(INPUT_DIR, input_items[0])
        with open(single_file_path, "rb") as file:
            data = file.read()
        encrypted_data = fernet.encrypt(data)

        # Save encrypted file
        encrypted_file = os.path.join(OUTPUT_DIR, input_items[0] + ".enc")
        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)

        print(f"Encrypted single file saved to {encrypted_file}")
        os.remove(single_file_path)

    else:
        # Folder or multiple files in Input folder
        create_zip(INPUT_DIR, TEMP_ARCHIVE)
        print(f"Folder compressed to {TEMP_ARCHIVE}")

        # Read and encrypt the zip file
        with open(TEMP_ARCHIVE, "rb") as file:
            data = file.read()
        encrypted_data = fernet.encrypt(data)

        # Save the encrypted data
        encrypted_file = os.path.join(OUTPUT_DIR, "encrypted_data.enc")
        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)
        print(f"Encrypted file saved to {encrypted_file}")

        # Clean up the temporary zip file and input folder
        os.remove(TEMP_ARCHIVE)
        shutil.rmtree(INPUT_DIR)
        os.makedirs(INPUT_DIR, exist_ok=True)

def decipher_folder_or_file():
    """
    Decrypts and extracts a folder or single file from an encrypted file in INPUT_DIR.
    """
    password = input("Enter the key: ")
    key = derive_key_from_password(password)
    fernet = Fernet(key)

    input_items = os.listdir(INPUT_DIR)
    if not input_items:
        print("Input folder is empty.")
        return

    encrypted_file_path = os.path.join(INPUT_DIR, input_items[0])

    # Check if it's a single encrypted file
    with open(encrypted_file_path, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print(f"Decryption failed: {e}")
        return

    if input_items[0].endswith(".enc") and input_items[0] != "encrypted_data.enc":
        # Single file decryption
        decrypted_file = os.path.join(OUTPUT_DIR, input_items[0].replace(".enc", ""))
        with open(decrypted_file, "wb") as file:
            file.write(decrypted_data)
        print(f"Decrypted single file saved to {decrypted_file}")

    else:
        # Folder decryption
        # Save the decrypted data as a zip file
        with open(TEMP_ARCHIVE, "wb") as file:
            file.write(decrypted_data)
        print(f"Decrypted to temporary zip: {TEMP_ARCHIVE}")

        # Extract the zip file
        extract_zip(TEMP_ARCHIVE, OUTPUT_DIR)
        print(f"Decrypted folder structure restored in {OUTPUT_DIR}")
        os.remove(TEMP_ARCHIVE)

    # Clean up encrypted file
    os.remove(encrypted_file_path)

def main():
    print("Folder/File Cipher/Decipher App")
    print("1. Cipher folder or file")
    print("2. Decipher folder or file")
    choice = input("Choose an option (1/2): ")

    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if choice == "1":
        cipher_folder_or_file()
    elif choice == "2":
        decipher_folder_or_file()
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
