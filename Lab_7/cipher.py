class Cipher:
    '''Represents a cipher class that encrypts and decrypts
    Attributes:
        _alphabet(str): a string of the alphabet letters
    '''
    
    def __init__(self):
        '''Initializes the alphabet string'''
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt_message(self, message):
        '''Returns an encrypted message'''
        s = ""
        for letter in message.upper():
            if letter.isalpha():
                s += self._encrypt_letter(letter)
            else:
                s += letter
        return s

    def decrypt_message(self, message):
        '''Returns a decrypted message'''
        s = ""
        for letter in message.upper():
            if letter.isalpha():
                s += self._decrypt_letter(letter)
            else:
                s += letter
        return s
        
    def _encrypt_letter(self, letter):
        '''Encrypts each letter in a message'''
        pos = self._alphabet.index(letter)
        return self._alphabet[25-pos]

    def _decrypt_letter(self, letter):
        '''Decrypts each letter in a message'''
        pos = self._alphabet.index(letter)
        return self._alphabet[25-pos]

if __name__ == "__main__":
    obj = Cipher()
    '''print(obj.encrypt_message("abc def"))
    print(obj.decrypt_message("ZYX wvu"))'''