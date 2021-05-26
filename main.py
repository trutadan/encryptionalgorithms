from caesarcipher import caesar_encrypt, caesar_decrypt
from railfencecipher import railfence_encrypt, railfence_decrypt
from morsecipher import *
from transpositioncipher import *
from affinecipher import *
from baconiancipher import *
from atbashcipher import *


def main():
    invalid = 0

    question1 = input("Do you want to encrypt/decrypt a text?\n"
                      "Type 'encrypt' or 'decrypt' in the next field: ")

    if question1.lower() == 'encrypt':
        question2 = input("What method do you want to use?\n"
        "Choose between 'atbash', 'caesar', 'morse', 'transposition', 'rail fence', 'baconian' or 'affine'. ")

        if question2.lower() == 'caesar':
            # caesar cipher encryption for all keys
            plainText = input("Enter your plain text you want to encrypt: ")
            print("Caesar cipher encryption:")
            for i in range(25):
                print(f"key #{i + 1}: " + caesar_encrypt(plainText, i))

        elif question2.lower() == 'morse':
            # morse cipher encryption
            plainText = input("Enter your plain text you want to encrypt(only CAPITALS): ")
            print(f"Morse cipher encryption: \n{morse_encrypt(plainText)}")

        elif question2.lower() == 'transposition':
            # transposition cipher encryption
            plainText = input("Enter your plain text you want to encrypt: ")
            maxKey = 7
            if len(plainText) < maxKey:
                maxKey = len(plainText)-2
            for i in range(maxKey):
                myKey = i + 2
                print(f"key #{myKey}: " + transposition_encrypt(myKey, plainText))

        elif question2.lower() == 'rail fence':
            # rail fence cipher encryption
            plainText = input("Enter your plain text you want to encrypt: ")
            plainText = str(plainText)
            i = 2
            while i < len(plainText):
                print(f"key #{i}: " + railfence_encrypt(plainText, i))
                i += 1

        elif question2.lower() == 'baconian':
            # baconian encryption
            plainText = input("Enter your plain text you want to encrypt: ")
            print("Baconian encryption: \n" + baconian_encrypt(plainText.upper()))

        elif question2.lower() == 'affine':
            # affine cipher encryption
            plainText = input("Enter your plain text you want to encrypt: ")
            myKey = getRandomKey()
            translated = affine_encrypt(myKey, plainText)
            print('Random key: %s' % (myKey))
            print("Encrypted text: " + translated)

        elif question2.lower() == 'atbash':
            # atbash cipher
            plainText = input("Enter your plain text you want to encrypt: ")
            print("Atbash encrypted text: " + atbash_cryption(plainText.upper()))

        else:
            invalid = 1

    elif question1.lower() == 'decrypt':
        question2 = input("What method do you want to use?\n"
        "Choose between 'caesar', 'atbash', 'morse', 'transposition', 'baconian' or 'rail fence'. ")

        if question2.lower() == 'caesar':
            # caesar cipher decryption for all keys
            plainText = input("Enter your plain text you want to decrypt: ")
            print("Caesar cipher decryption:")
            for i in range(25):
                print(f"key #{i+1}: " + caesar_decrypt(plainText, i+1))

        elif question2.lower() == 'morse':
            # morse cipher decryption
            plainText = input("Enter your plain text you want to decrypt: ")
            print(f"Morse cipher decryption: \n{morse_decrypt(plainText)}")

        elif question2.lower() == 'transposition':
            # transposition cipher decryption for all keys
            plainText = input("Enter your plain text you want to decrypt: ")
            maxKey = 7
            if len(plainText) < maxKey:
                maxKey = len(plainText) - 2
            for i in range(maxKey):
                myKey = i + 2
                print(f"key #{myKey}: " + transposition_decrypt(myKey, plainText))

        elif question2.lower() == 'rail fence':
            # rail fence decryption
            plainText = input("Enter your plain text you want to decrypt: ")
            plainText = str(plainText)
            i = 2
            while i < len(plainText):
                print(f"key #{i}: " + railfence_decrypt(plainText, i))
                i += 1

        elif question2.lower() == 'baconian':
            # baconian decryption
            plainText = input("Enter your plain text you want to decrypt: ")
            print("Baconian decryption(uppercase version): \n" + baconian_decrypt(plainText.lower()))

        elif question2.lower() == 'atbash':
            # atbash cipher
            plainText = input("Enter your plain text you want to decrypt: ")
            print("Atbash decrypted text(uppercase version): " + atbash_cryption(plainText.upper()))

        else:
            invalid = 1

    else:
        invalid = 1


    if invalid == 1:
        print("Wrong input! Try again.")

    input()

if __name__ == '__main__':
    main()