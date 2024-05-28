import argparse
import os
import encryptor as encryptor  # Ensure that 'encryptor' is a module in the same directory or installed


def create_file(file_name: str) -> str:
    """
    Creates a file with dummy data for testing encryption functionality.

    :param file_name: Name of the file to create.
    :return: The name of the created file.
    """
    try:
        with open(file_name, 'x') as demoFile:
            demoFile.write(
                "This file was created to test the encryption functionality with dummy data.\n"
                "Bank-Login:\tadmin\nPW:\t\tCashMoney1"
            )
            print("File created")
            return file_name
    except FileExistsError:
        print("File already exists, removing existing file and creating a new one.")
        os.remove(file_name)
        return create_file(file_name)


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Ransomware Simulator by Naveen A.")
    parser.add_argument("file", help="File to encrypt or decrypt.")
    parser.add_argument("--enc", action="store_true", help="Encrypt the specified file.")
    parser.add_argument("--dec", action="store_true", help="Decrypt the specified file.")
    args = parser.parse_args()

    # Extract file name from arguments
    file = args.file

    print(args)

    # Perform encryption or decryption based on the provided arguments
    if args.enc:
        # Uncomment the following line if you want to create a new file before encryption
        # create_file(file)
        encryptor.file_encrypt(file)
    elif args.dec:
        encryptor.file_decrypt(file)
