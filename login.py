import cipher
from pathlib import Path

# Opens files .cipher and .val.
# .cipher and .val are the hidden system files.
login_file = Path(".cipher")
key_file = Path(".val")
log_file = Path("log.txt")

if not (login_file.is_file() or key_file.is_file() or log_file.is_file()):
    password = open(".cipher", "w+", encoding = "utf=8")
    key = open(".val", "w+", encoding = "utf-8")
    log = open("log.txt", "w+", encoding = "utf-8")
    # Closes the log.txt file I/O instance because it is not required in this file.
    # log.txt is used again in shell.py file.
    log.close()
    while True:
        try:
            # Asks the user to set up a new password.
            new_password = input("\nNew Login Password: ")
            break
        except KeyboardInterrupt:
            print()
    while True:
        try:
            # Asks the user to set up a new encryption key.
            cipher_key = int(input("\nNew Encryption Key: "))
            key.write(str(cipher_key))
            print()
            break
        except ValueError:
            print("\nInvalid Key Entered.")
            continue
        except KeyboardInterrupt:
            print()
    key.close()
    # Encrypts the new password with the key entered by the user.
    password.write(cipher.enc(new_password, cipher_key))
# Asks user to log in with password if the files cipher and val exist.
elif login_file.is_file() or key_file.is_file():
    password = open(".cipher", "r", encoding = "utf-8")
    login_password = password.read()
    key = open(".val", "r", encoding = "utf-8")
    cipher_key = int(key.read())
    while True:
        try:
            ask_password = input("\nLogin Password: ")
            # Checks if the entered password matches the correct decrypted password.
            if ask_password == cipher.dec(login_password, cipher_key):
                print("\nWelcome to Explore.\n")
                break
            else:
                print("\nAccess Denied.")
                continue
        except KeyboardInterrupt:
            print("\n\nBye.\n")
            break
    password.close()
    key.close()
