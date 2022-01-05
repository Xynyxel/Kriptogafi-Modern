from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import helpers


class MenuScreen(Screen):
    pass


class RC4Screen(Screen):
  def encodeData(self):
    cipher_text = self.cipher_text.text
    key_cipher_text = self.key_cipher_text.text
    print(cipher_text)
    print(key_cipher_text)


class RSAScreen(Screen):
    pass


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
