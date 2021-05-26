global morseAlphabet

morseAlphabet = {
    "A": ".-",    "B": "-...",    "C": "-.-.",    "D": "-..",    "E": ".",    "F": "..-.",
    "G": "--.",    "H": "....",    "I": "..",    "J": ".---",    "K": "-.-",    "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",    "P": ".--.",    "Q": "--.-",    "R": ".-.",
    "S": "...",    "T": "-",    "U": "..-",    "V": "...-",    "W": ".--",    "X": "-..-",
    "Y": "-.--",    "Z": "--..",
    "1": ".----",    "2": "..---",    "3": "...--",    "4": "....-",    "5": ".....",
    "6": "-....",    "7": "--...",    "8": "---..",    "9": "----.",    "0": "-----",
    ".": ".-.-.-",    ",": "--..--",    ":": "---...",    "?": "..--..",    "'": ".----.",
    "-": "-....-",    "/": "-..-.",    "@": ".--.-.",    "=": "-...-",    " ": "/",
    ";": "-.-.-",    "_": "..--.-",    "+": ".-.-.",    "(": "-.--.",    ")": "-.--.-",
                }


def morse_encrypt(text):
    ciphertext = ""
    for letter in text:
        if letter != ' ':
            # looks up the dictionary and adds the
            # corresponding morse code, along with
            # a space at the end of the word
            ciphertext += morseAlphabet[letter] + ' '
        else:
            # adds 2 spaces between the words
            ciphertext += ' '
    return ciphertext


def morse_decrypt(text):
    text += ' '
    plaintext = ''
    code = ''

    for letter in text:
        # checks for space
        if letter != ' ':
            # the space counter
            ok = 0
            code += letter
        # in case of space
        else:
            # indicates the appearance of a new word/a new character
            ok += 1
            if ok == 2:
                # adding space to separate words
                plaintext += ' '
            else:
                # access the keys by their values
                plaintext += list(morseAlphabet.keys())[list(morseAlphabet.values()).index(code)]
                code = ''
    return plaintext