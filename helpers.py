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
    cipher_text : cipher_text
    key_cipher_text : key_cipher_text
    MDLabel:
        text: 'Encryption RC4'
        halign: 'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.8}
    MDTextField:
        hint_text: "Enter Plain Text"
        helper_text: "Todo Encryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.3, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text: "Enter key"
        helper_text: "Todo Encryption"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.3, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Encryption'
        pos_hint: {'center_x':0.3,'center_y':0.5}
        on_press: 

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
        on_press: root.encodeData()
    
            
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.1,'center_y':0.9}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = "right"
        
<RSAScreen>:
    name: 'RSA'
    MDLabel:
        text: 'RSA'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = "right"
        
""" 