global baconianDictionary

baconianDictionary = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
                      'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
                      'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
                      'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
                      'U': 'babaa', 'V': 'babab', 'W': 'babaa', 'X': 'babab', 'Y': 'babba',
                      'Z': 'babbb', ' ': ' '}

def baconian_encrypt(text):
    ciphertext = ''
    for letter in text:
        # checks for space
        if (letter != ' '):
            # adds the ciphertext corresponding to the
            # plaintext from the dictionary
            ciphertext += baconianDictionary[letter]
        else:
            # adds space
            ciphertext += ' '

    return ciphertext


def baconian_decrypt(text):
    plaintext = ''
    i = 0

    while True:
        # condition to run decryption till
        # the last set of ciphertext
        if (i < len(text) - 4):
            # extracting a set of ciphertext
            # from the text
            substr = text[i:i + 5]
            # checking for space as the first
            # character of the substring
            if (substr[0] != ' '):
                plaintext += list(baconianDictionary.keys())[list(baconianDictionary.values()).index(substr)]
                # to get the next set of ciphertext
                i += 5

            else:
                # adds space
                plaintext += ' '
                # index next to the space
                i += 1
        else:
            break

    return plaintext