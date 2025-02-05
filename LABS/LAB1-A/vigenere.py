from text_cleaner import text_cleaner

class Vigenere():
    def __init__(self, keyword):
        self.keyword = keyword
        self.alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    
    def encrypt(self, message):
        encrypted = ''
        text = text_cleaner(message)
        keyword_index = 0

        for char in text:  
            if char in self.alphabet:
                shift = self.alphabet.index(self.keyword[keyword_index])
                encrypted_index = (self.alphabet.index(char) + shift) % len(self.alphabet)
                encrypted += self.alphabet[encrypted_index]

                keyword_index = (keyword_index + 1) % len(self.keyword)
            else:
                encrypted += char
        
        return encrypted

    def decrypt(self, message):
        decrypted = ''
        keyword_index = 0

        for char in message:
            if char in self.alphabet:
                shift = self.alphabet.index(self.keyword[keyword_index])
                decrypted_index = (self.alphabet.index(char) - shift) % len(self.alphabet)
                decrypted += self.alphabet[decrypted_index]

                keyword_index = (keyword_index + 1) % len(self.keyword)
            else:
                decrypted += char
        
        return decrypted