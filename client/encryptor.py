import getpass as gt

import requests
from cryptography.fernet import Fernet


def __key_load(new: bool):
    user = gt.getuser()
    if new:
        response = requests.get("http://127.0.0.1:5000/key",
                                params={"user": user})
    else:
        response = requests.get(f"http://127.0.0.1:5000/key/{user}")
    # print(response.content)
    return response.content


def file_encrypt(original_file):
    key = __key_load(True)
    print(key)
    f = Fernet(key)

    with open(original_file, 'rb+') as file:
        original = file.read()
        encrypted = f.encrypt(original)
        file.seek(0)
        file.write(encrypted)
        file.truncate()
        print(original_file + ' successfully encrypted!')


def file_decrypt(encrypted_file):
    key = __key_load(False)
    print(key)
    f = Fernet(key)

    with open(encrypted_file, 'rb+') as file:
        encrypted = file.read()
        decrypted = f.decrypt(encrypted)
        file.seek(0)
        file.write(decrypted)
        file.truncate()
        print(encrypted_file + ' successfully decrypted!')
