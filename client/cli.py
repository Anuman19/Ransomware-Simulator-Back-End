import argparse
import os

import encryptor as encryptor


def create_file(file_name: str) -> str:
    try:
        with open(file_name, 'x') as demoFile:
            demoFile.write(
                "This file was created to test the encryption functionality with dummy data.\nBank-Login:\tadmin\nPW:\t\tCashMoney1")
            print("file created")
            return file_name
    except FileExistsError:
        print("File already exists")
        os.remove(file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Ransomware Simulator by Naveen A.""")
    parser.add_argument("file", help="File to encrypt or decrypt.")
    parser.add_argument("--enc", action="store_true", help="Encrypt a file.")
    parser.add_argument("--dec", action="store_true", help="Decrypt a file.")
    args = parser.parse_args()
    file = args.file
    print(args)
    if args.enc:
        create_file(file)
        encryptor.file_encrypt(file)
    elif args.dec:
        encryptor.file_decrypt(file)
