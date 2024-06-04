# Ransomware Simulator

The Ransomware Simulator, created by Naveen A., is an educational project designed to provide insight into the operation
of ransomware. Ransomware is a type of malicious software that encrypts files on a victim's computer and demands
payment (a "ransom") for their decryption. This simulator demonstrates how ransomware functions by allowing users to
encrypt and decrypt files using Python and the `cryptography` library. Through hands-on experimentation, users can learn
about ransomware's mechanisms and understand the importance of implementing robust cybersecurity measures.

## Features

- **File Encryption**: Utilizes a generated encryption key to encrypt a specified file securely.
- **File Decryption**: Decrypts a previously encrypted file using the stored encryption key, restoring it to its
  original state.
- **Key Management**: Facilitates the generation and retrieval of encryption keys associated with individual users,
  ensuring secure data handling.
- **File Creation**: Generates a file with dummy data specifically designed for testing encryption and decryption
  functionalities.

## Requirements

- Python 3.x

Dependencies are listed in the `requirements.txt` file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anuman19/Ransomware-Sim.git
   
2. Create a virtual environment and install requirements:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Start the Flask App:
    ```bash
    python app.py

4. Ensure JSON Files are empty:
    ```bash
    vi db.json
    vi creds.json
   
5. Interact with the CLI:
    ```bash
    python cli.py <file> --enc
    python cli.py <file> --dec

6. Access API Endpoints:
    ```bash
    curl 127.0.0.1:5000/key
    curl 127.0.0.1:5000/keys

## Command-Line Interface (CLI) Integration

### `cli.py`

The `cli.py` script provides a command-line interface (CLI) for interacting with the Ransomware Simulator. It allows users to encrypt and decrypt files through a terminal or command prompt, providing a convenient way to perform these operations.

### Usage

1. **File Creation**:
    - The `create_file()` function creates a file with dummy data for testing encryption functionality. This file contains sample text simulating sensitive information like bank login credentials.

2. **Argument Parsing**:
    - The script uses the `argparse` module to parse command-line arguments. It accepts the following arguments:
        - `file`: Specifies the file to encrypt or decrypt.
        - `--enc`: Encrypts the specified file.
        - `--dec`: Decrypts the specified file.

3. **Encryption/Decryption**:
    - Based on the provided arguments, the script either encrypts or decrypts the specified file using the `file_encrypt()` or `file_decrypt()` functions from the `encryptor` module.
    - If encryption or decryption is successful, the script displays a message indicating the operation's completion.

4. **User Interaction**:
    - Users interact with the CLI by executing the script and providing appropriate arguments in the terminal or command prompt.
    - For encryption, users specify the file to encrypt using the `--enc` flag.
    - For decryption, users specify the file to decrypt using the `--dec` flag.

5. **Error Handling**:
    - The script handles exceptions gracefully and displays error messages if encryption or decryption fails.

The `cli.py` script provides a straightforward way to interact with the Ransomware Simulator via the command line, allowing users to encrypt and decrypt files efficiently without the need for a graphical interface.


## GUI Integration

### `gui.py`

The `gui.py` script provides a graphical user interface (GUI) for interacting with the Ransomware Simulator. It allows users to encrypt and decrypt files through a simple and intuitive interface built using the Tkinter library in Python.

### Usage

1. **File Creation**:
    - The `create_file()` function creates a file with dummy data for testing encryption functionality. This file contains sample text simulating sensitive information like bank login credentials.

2. **File Encryption**:
    - The `encrypt_file()` function prompts the user to select a file using a file dialog. Once a file is selected, it invokes the `file_encrypt()` function from the `encryptor` module to encrypt the selected file.
    - After encryption is complete, a message box displays a notification indicating that the file has been encrypted successfully.

3. **File Decryption**:
    - The `decrypt_file()` function works similarly to the `encrypt_file()` function but for decryption. It prompts the user to select an encrypted file and decrypts it using the `file_decrypt()` function from the `encryptor` module.
    - Upon successful decryption, a message box notifies the user that the file has been decrypted.

4. **User Interface**:
    - The script creates a main window using Tkinter and adds buttons for encrypting and decrypting files.
    - When the user clicks the "Encrypt File" button, the `encrypt_file()` function is called.
    - Similarly, when the user clicks the "Decrypt File" button, the `decrypt_file()` function is called.

5. **Event Loop**:
    - The script enters the Tkinter event loop, allowing users to interact with the GUI. It remains active until the user closes the window.

The `gui.py` script provides a convenient and user-friendly way to interact with the Ransomware Simulator, making it accessible to users who prefer a graphical interface over a command-line interface.

