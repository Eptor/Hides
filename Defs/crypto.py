import pyAesCrypt
from os import stat, remove, path
from pathlib import Path
import glob


def encrypt(file, password):
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    # encrypt
    with open(file, "rb") as fIn:
        with open(f"{file}.crypto", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

    return f"{file}.crypto"


def decrypt(lista, password):

    bufferSize = 64 * 1024
    # decrypt
    for file in lista:
        try:
            with open(file, "rb") as fIn:
                with open(file[:-7], "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(
                        fIn, fOut, password, bufferSize, stat(file).st_size
                    )
        except Exception as e:
            print(e)
        else:
            remove(file)
