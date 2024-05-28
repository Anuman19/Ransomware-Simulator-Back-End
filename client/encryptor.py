import getpass as gt
import requests
from cryptography.fernet import Fernet


def __key_load(new: bool):
    """
    Load the encryption/decryption key for the current user.

    :param new: If True, generate a new key. Otherwise, load the existing key.
    :return: The key in bytes.
    """
    user = gt.getuser()  # Get the current user's username
    if new:
        # Request to generate a new key for the user
        response = requests.get("http://127.0.0.1:5000/key", params={"user": user})
    else:
        # Request to load the existing key for the user
        response = requests.get(f"http://127.0.0.1:5000/key/{user}")

    # Check for request success
    response.raise_for_status()
    return response.content


def file_encrypt(original_file):
    """
    Encrypt a file using a newly generated key.

    :param original_file: Path to the original file to be encrypted.
    """
    key = __key_load(True)  # Load a new encryption key
    f = Fernet(key)

    with open(original_file, 'rb+') as file:
        original = file.read()  # Read the original file content
        encrypted = f.encrypt(original)  # Encrypt the content
        file.seek(0)  # Move to the beginning of the file
        file.write(encrypted)  # Write the encrypted content
        file.truncate()  # Truncate the file to the new length
        print(f"{original_file} successfully encrypted!")


def file_decrypt(encrypted_file):
    """
    Decrypt a previously encrypted file using the stored key.

    :param encrypted_file: Path to the encrypted file to be decrypted.
    """
    key = __key_load(False)  # Load the existing decryption key
    f = Fernet(key)

    with open(encrypted_file, 'rb+') as file:
        encrypted = file.read()  # Read the encrypted file content
        decrypted = f.decrypt(encrypted)  # Decrypt the content
        file.seek(0)  # Move to the beginning of the file
        file.write(decrypted)  # Write the decrypted content
        file.truncate()  # Truncate the file to the new length
        print(f"{encrypted_file} successfully decrypted!")
