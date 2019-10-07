import os
import sys
import toml
from cryptography.fernet import Fernet


def encrypt(toml_path, key):
    if isinstance(key, str):
        key = key.encode('ascii')

    with open(toml_path) as toml_file:
        data = toml_file.read().encode('utf-8')

    encrypted_data =  Fernet(key).encrypt(data)
    return encrypted_data


def decrypt(bin_path, key):
    if isinstance(key, str):
        key = key.encode('ascii')

    with open(bin_path, 'rb') as bin_file:
        encrypted_data = bin_file.read()

    data = Fernet(key).decrypt(encrypted_data).decode('utf-8')
    return toml.loads(data)


if __name__ == '__main__':
    what, input_path, *_ = sys.argv[1:]
    what = what.lower().strip()
    key = os.getenv('CVKEY')
    if what == 'encrypt':
        print(encrypt(input_path, key).decode('ascii'))
    elif what == 'decrypt':
        print(toml.dumps(decrypt(input_path, key)))
