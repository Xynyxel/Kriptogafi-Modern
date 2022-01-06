screen_helper = """
ScreenManager:
    MenuScreen:
    RC4Screen:
    RSAScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Enkripsi Simetris - RC4'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: 
            root.manager.current = 'RC4'
            root.manager.transition.direction = "left" 
    MDRectangleFlatButton:
        text: 'Enkripsi Asimetris - RSA'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: 
            root.manager.current = 'RSA'
            root.manager.transition.direction = "left"    

<RC4Screen>:
    name: 'RC4'
    plain_text : plain_text
    key_plain_text : key_plain_text
    cipher_text : cipher_text
    key_cipher_text : key_cipher_text
    hasil_enkripsi : hasil_enkripsi
    hasil_dekripsi : hasil_dekripsi
    
    
    MDLabel:
        text: 'Encryption RC4'
        halign: 'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.8}
    MDTextField:
        id: plain_text
        hint_text: "Enter Plain Text"
        helper_text: "Todo Encryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.3, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: key_plain_text
        hint_text: "Enter key"
        helper_text: "Todo Encryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.3, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Encryption'
        pos_hint: {'center_x':0.3,'center_y':0.5}
        on_press: root.encodeData() 
    MDLabel:
        id: hasil_enkripsi
        text: 'Hasil Enkripsi RC4'
        halign: 'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.4}

    MDLabel:
        text: 'Decryption RC4'
        halign: 'center'
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}
    MDTextField:
        id: cipher_text
        hint_text: "Enter Cipher Text"
        helper_text: "Todo Decryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.8, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: key_cipher_text
        hint_text: "Enter key"
        helper_text: "Todo Decryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.8, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Decryption'
        pos_hint: {'center_x':0.8,'center_y':0.5}
        on_press: root.decodeData()
    MDLabel:
        id: hasil_dekripsi
        text: 'Hasil Dekripsi RC4'
        halign: 'center'
        pos_hint:{'center_x': 0.8, 'center_y': 0.4}
    
            
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.1,'center_y':0.9}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = "right"
            root.close()
        
<RSAScreen>:
    name: 'RSA'
    plain_text : plain_text
    cipher_text : cipher_text
    hasil_enkripsi : hasil_enkripsi
    hasil_dekripsi : hasil_dekripsi
    publickey : publickey
    privatekey : privatekey

    MDLabel:
        text: 'Encryption RSA'
        halign: 'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.8}
    MDTextField:
        id: plain_text
        hint_text: "Enter Plain Text"
        helper_text: "Todo Encryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.3, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDLabel:
        id: publickey
        text: 'Public Key'
        halign: 'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.6}
    MDRectangleFlatButton:
        text: 'Encryption'
        pos_hint: {'center_x':0.3,'center_y':0.4}
        on_press: root.encodeData()
    MDTextField:
        id: hasil_enkripsi
        multiline: True
        helper_text_mode: "on_focus"
        text: 'Hasil Enkripsi RSA'
        pos_hint:{'center_x': 0.3, 'center_y': 0.3} 
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text: 'Generate Public and Private Key'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.Generatepublickey_private()

    MDLabel:
        text: 'Decryption RSA'
        halign: 'center'
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}
    MDTextField:
        id: cipher_text
        hint_text: "Enter Cipher Text"
        helper_text: "Todo Decryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.8, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDLabel:
        id: privatekey
        text: 'Private Key'
        halign: 'center'
        pos_hint:{'center_x': 0.8, 'center_y': 0.6}
    MDRectangleFlatButton:
        text: 'Decryption'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.decodeData()
    MDLabel:
        id: hasil_dekripsi
        text: 'Hasil Dekripsi RSA'
        halign: 'center'
        pos_hint:{'center_x': 0.8, 'center_y': 0.3}

    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.1,'center_y':0.9}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = "right"
            root.close()
        
""" 