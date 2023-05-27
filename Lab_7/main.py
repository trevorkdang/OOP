# Name: Co Chau and Trevor Dang
# Group: 8
# Date: 10/6/22
# Description: This is a program that encrypts and decrypts provided strings and gives the option to shift a message by a certain amount of units.

import check_input
from cipher import Cipher
from caesar_cipher import CaesarCipher

def main():
    '''This function runs a program that can encrypt and decrypt messages by using reversed indexes'''
    file_name = r"Lab_7/message.txt"
    choice = check_input.get_int_range("Secret Decoder Ring:\n1. Encrypt\n2. Decrypt\n", 1, 2)

    if choice == 1:
        with open(file_name, "w") as file:
            encryption = check_input.get_int_range("Enter encryption type:\n1. Atbash\n2. Caesar\n", 1, 2)
            message = input("Enter message: ")
            if encryption ==  1:
                encrypt = Cipher().encrypt_message(message)
                file.write(encrypt)
            else:
                shift_val = check_input.get_int_range("Enter shift value: ", 0, 25) 
                encrypt = CaesarCipher(shift_val).encrypt_message(message)
                file.write(encrypt)
        print('Encrypted message saved to "message.txt"')

    else:
        decryption = check_input.get_int_range("Enter decryption type:\n1. Atbash\n2. Caesar\n", 1, 2)
        with open(file_name, "r") as file:
            encrypt_mess = file.read()
            if decryption == 1:
                decrypt = Cipher().decrypt_message(encrypt_mess)
            else:
                shift_val1 = check_input.get_int_range("Enter shift value: ", 0, 25)
                decrypt = CaesarCipher(shift_val1).decrypt_message(encrypt_mess)
        print('Reading encrypted message from "message.txt". \nDecrypted message: {}'.format(decrypt))


            
if __name__ == "__main__":
    main()

