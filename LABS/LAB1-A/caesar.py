from text_cleaner import text_cleaner

class Ceasar():
    def __init__(self, key):
        self.key = key
        self.alphabet = 'abcdefghijklmnñopqrstuvwxyz'

    
    def encrypt(self, message):
        encrypted = ""
        text = text_cleaner(message)
        for letter in text:
            if letter == " ":
                encrypted += " "
            else:
                encrypted += self.alphabet[(self.alphabet.index(letter) + self.key) % 26]
        return encrypted

    def c_decrypt(self, message):
        decrypted = ""
        for letter in message:
            if letter == " ":
                decrypted += " "
            else:
                decrypted += self.alphabet[(self.alphabet.index(letter) - self.key) % 26]
        return decrypted
    