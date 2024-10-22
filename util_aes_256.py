import base64
from Crypto import Random
from Crypto.Cipher import AES


class Cipher:

    def __init__(self, key, iv):
        self.bs = 16
        #self.key = key
        self.key = key.encode('utf-8')
        self.key = Cipher.str_to_bytes(key)
        #self.iv = iv
        self.iv = iv.encode('utf-8')
        self.iv = Cipher.str_to_bytes(iv)

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def encrypt(self, plain_text):
        #print(f'plain_text: {plain_text}')

        pad_text = self._pad(plain_text)
        #print(f'pad_text: {pad_text}')
        #print(f'len(pad_text): {len(pad_text)}')

        pad_text_bytes = self.str_to_bytes(pad_text)
        #print(f'pad_text_bytes: {pad_text_bytes}')
        #print(f'len(pad_text_bytes): {len(pad_text_bytes)}')

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        cipher_text = cipher.encrypt(pad_text_bytes)
        #print(f'cipher_text: {cipher_text}')

        base64_text = base64.b64encode(cipher_text)
        #print(f'base64_text: {base64_text}')

        return base64_text

    def decrypt(self, cipher_text):
        cipher_text = base64.b64decode(cipher_text)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self._unpad(cipher.decrypt(cipher_text))

    def _pad(self, s):
        return s + (self.bs - len(s.encode('utf-8')) % self.bs) * chr(self.bs - len(s.encode('utf-8')) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
