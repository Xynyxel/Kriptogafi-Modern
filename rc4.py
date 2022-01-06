from Crypto.Cipher import ARC4 as rc4cipher
import base64

def encode(data, key1):
	key = bytes(key1, encoding='utf-8')
	enc = rc4cipher.new(key)
	res = enc.encrypt(data.encode('utf-8'))
	res=base64.b64encode(res)
	res = str(res,'utf8')
	return res

def decode(data, key1):
	data = base64.b64decode(data)
	key = bytes(key1, encoding='utf-8')
	enc = rc4cipher.new(key)
	res = enc.decrypt(data)
	res = str(res,'utf8')
	return res

# print(encode("andra","1 1 1 1 1 1 1"))
# print(decode("UCAOjEo=","1 1 1 1 1 1 1"))