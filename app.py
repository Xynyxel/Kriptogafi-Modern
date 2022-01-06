from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import helpers
import rc4
import rsa
import binascii

class MenuScreen(Screen):
    pass


class RC4Screen(Screen):
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

    def Generatepublickey(self):
        publickey = rsa.publickey
        print(publickey)
        self.publickey.text = "test"

    def Generateprivatekey(self):
        self.privatekey.text =  rsa.privatekey

    def encodeData(self):
        plain_text = self.plain_text.text
        output  = str(rsa.encode(plain_text))
        self.hasil_enkripsi.text = output
    
    def decodeData(self):
        cipher_text = self.cipher_text.text
        output  = "Hasil Dekripsi : "+rsa.decode(cipher_text)
        self.hasil_dekripsi.text = output


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
