from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import helpers
import rc4
import rsa
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class MenuScreen(Screen):
    pass


class RC4Screen(Screen):

    def close(self):
        self.plain_text.text = ""
        self.key_plain_text.text = ""
        self.hasil_enkripsi.text = ""
        self.cipher_text.text = ""
        self.key_cipher_text = ""    
        self.hasil_dekripsi = ""

    def encodeData(self):
        plain_text = self.plain_text.text
        key_plain_text = self.key_plain_text.text
        hasil = rc4.encode(plain_text, key_plain_text)
        output  = "Hasil Enkripsi : "+hasil
        self.hasil_enkripsi.text = output
    
    def decodeData(self):
        cipher_text = self.cipher_text.text
        key_cipher_text = self.key_cipher_text.text
        hasil = rc4.decode(cipher_text, key_cipher_text)
        output  = "Hasil Dekripsi : "+hasil
        self.hasil_dekripsi.text = output


class RSAScreen(Screen):

    def close(self):
        self.plain_text = ""
        self.cipher_text = ""
        self.hasil_enkripsi = ""
        self.hasil_dekripsi = ""
        self.publickey = ""
        self.privatekey = ""

    def Generatepublickey_private(self):
        keyPair = RSA.generate(3072)
        pubKey = keyPair.publickey()
        pubKeyPEM = pubKey.exportKey()
        privKeyPEM = keyPair.exportKey()
        self.publickey.text = pubKeyPEM.decode('ascii')
        self.privatekey.text = privKeyPEM.decode('ascii')

    # def encodeData(self):
    #     pubKey = ""
    #     plain_text = self.plain_text.text
    #     plain_text = bytes(plain_text, 'utf-8')
    #     encryptor = PKCS1_OAEP.new(pubKey)
    #     encrypted = encryptor.encrypt(plain_text)
    #     self.hasil_enkripsi.text = binascii.hexlify(encrypted).decode('UTF-8')
    
    # def decodeData(self):
    #     keypair = ""
    #     cipher_text = self.cipher_text.text
    #     decryptor = PKCS1_OAEP.new(keyPair)
    #     decrypted = decryptor.decrypt(cipher_text)
    #     self.hasil_dekripsi.text = decrypted.decode('UTF-8')


class KriptografiModernApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        screen = Builder.load_string(helpers.screen_helper)
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(RC4Screen(name='RC4'))
        sm.add_widget(RSAScreen(name='RSA'))
        return screen


if __name__ == "__main__":
  KriptografiModernApp().run()
