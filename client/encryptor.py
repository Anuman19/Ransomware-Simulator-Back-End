import getpass as gt

import requests
from cryptography.fernet import Fernet


def key_load():
    user = gt.getuser()
    response = requests.get("http://127.0.0.1:5000/key",
                            params={"user": user})
    print(response.content)
    return response.content


def file_encrypt(key, original_file):
    f = Fernet(key)

    with open(original_file, 'r+') as file:
        original = file.read()
        encrypted = f.encrypt(original)
        file.seek(0)
        file.write(encrypted)
        file.truncate()


def file_decrypt(key, encrypted_file):
    f = Fernet(key)

    with open(encrypted_file, 'r+') as file:
        encrypted = file.read()
        decrypted = f.decrypt(encrypted)
        file.seek(0)
        file.write(decrypted)
        file.truncate()


