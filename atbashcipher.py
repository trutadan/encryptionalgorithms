global atbashDictionary

atbashDictionary = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}


def atbash_cryption(text):
    ciphertext = ''
    for letter in text:
        # checks for space
        if letter != ' ':
            # adds the corresponding letter from the atbashDictionary
            ciphertext += atbashDictionary[letter]
        else:
            # adds space
            ciphertext += ' '

    return ciphertext