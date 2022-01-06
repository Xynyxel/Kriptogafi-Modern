from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

enkripsi = ""

keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
privKeyPEM = keyPair.exportKey()

def encode(plain_text):
    plain_text = bytes(plain_text, 'utf-8')
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(plain_text)
    enkripsi = encrypted
    return encrypted
    # return binascii.hexlify(encrypted).decode('UTF-8')

def decode(cipher):
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(enkripsi)
    return decrypted.decode('UTF-8')

# print(encode("Tony"))
# print(decode(encode("Tony")))