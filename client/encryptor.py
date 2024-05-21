import getpass as gt

import requests
from cryptography.fernet import Fernet


def __key_load():
    user = gt.getuser()
    response = requests.get("http://127.0.0.1:5000/key",
                            params={"user": user})
    print(response.content)
    return response.content


def file_encrypt(original_file):
    key = __key_load()
    f = Fernet(key)

    with open(original_file, 'rb+') as file:
        original = file.read()
        encrypted = f.encrypt(original)
        file.seek(0)
        file.write(encrypted)
        file.truncate()
        print(original_file + ' successfully encrypted!')


def file_decrypt(encrypted_file):
    key = __key_load()
    f = Fernet(key)

    with open(encrypted_file, 'rb+') as file:
        encrypted = file.read()
        decrypted = f.decrypt(encrypted)
        file.seek(0)
        file.write(decrypted)
        file.truncate()
        print(encrypted_file + ' successfully decrypted!')
