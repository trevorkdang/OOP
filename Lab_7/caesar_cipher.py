from cipher import Cipher
class CaesarCipher(Cipher):
    '''Represents a cipher class that encrypts and decrypts with a shift value
    Attributes:
        shift(int): shifts the index of the alphabet
        _alphabet(str): a string of the alphabet letters'''
    
    def __init__(self, shift):
        '''Initializes the alphabet string and the shift value'''
        super().__init__()
        if type(shift) != int:
            raise TypeError("Must be integer")
        elif shift < 0:
            raise ValueError("Can't be negative number")
        else:
            self.shift = shift

    def _encrypt_letter(self, letter):
        '''Encrypts each letter in a message'''
        pos = self._alphabet.index(letter)
        if (pos+self.shift) >= 25:
             shift_pos = (pos+self.shift) - 26
        else:
            shift_pos = pos + self.shift
        return self._alphabet[shift_pos]

    def _decrypt_letter(self, letter):
        '''Decrypts each letter in a message'''
        pos = self._alphabet.index(letter)
        return self._alphabet[pos - self.shift]
        

if __name__ =="__main__":
    obj = CaesarCipher()
    '''print(obj.encrypt_message("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print(obj.decrypt_message("DEFGHIJKLMNOPQRSTUVWXYZABC"))'''

    