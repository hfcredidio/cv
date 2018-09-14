import os
import sys
import toml
from cryptography.fernet import Fernet


def encrypt(toml_path, out_path, key):
    if isinstance(key, str):
        key = key.encode('ascii')

    with open(toml_path) as toml_file:
        data = toml_file.read().encode('utf-8')

    encrypted_data =  Fernet(key).encrypt(data)
    with open(out_path, 'wb') as out_file:
        out_file.write(encrypted_data)


def decrypt(bin_path, key):
    if isinstance(key, str):
        key = key.encode('ascii')

    with open(bin_path, 'rb') as bin_file:
        encrypted_data = bin_file.read()

    data = Fernet(key).decrypt(encrypted_data).decode('utf-8')
    return toml.loads(data)


if __name__ == '__main__':
    toml_path, out_path, *_ = sys.argv[1:]
    key = os.getenv('CVKEY')
    encrypt(toml_path, out_path, key)
