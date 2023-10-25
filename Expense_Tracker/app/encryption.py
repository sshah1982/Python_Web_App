from cryptography.fernet import Fernet

from dotenv import dotenv_values

config = dotenv_values(".env")

ENC_KEY = config['ENC_KEY']


def generate_key():
    return str(Fernet.generate_key())


def encrypt_password(org_pwd):
    fernet = Fernet(ENC_KEY)
    enc_pwd = fernet.encrypt(org_pwd.encode())
    return enc_pwd


def decrypt_password(enc_pwd):
    fernet = Fernet(ENC_KEY)
    dec_pwd = fernet.decrypt(enc_pwd).decode()
    return dec_pwd
