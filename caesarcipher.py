def caesar_encrypt(text, key):
    ciphertext = ""
    # transverse the whole plain text
    for i in range(len(text)):
        character = text[i]
        # uppercase characteracters in plain text
        if (character.isupper()):
            ciphertext += chr((ord(character) + key - 64) % 26 + 65)
        # lowercase characteracters in plain text
        elif (character.islower()):
            ciphertext += chr((ord(character) + key - 96) % 26 + 97)
        # digit characteracters in plain text
        elif (character.isdigit()):
            ciphertext += str((int(character) + key + 1) % 10)
        # any non-digit/non-letter characteracters in plain text
        else:
            ciphertext += character

    return ciphertext


def caesar_decrypt(text, key):
    plaintext = ""
    # transverse the encrypted text
    for i in range(len(text)):
        character = text[i]
        # uppercase characters in encrypted text
        if (character.isupper()):
            plaintext += chr((ord(character) - ord('A') - key) % 26+ ord('A'))
        # lowercase characters in encrypted text
        elif (character.islower()):
            plaintext += chr((ord(character) - ord('a') - key) % 26+ ord('a'))
        # digit characters in encrypted text
        elif (character.isdigit()):
            plaintext += str((int(character) - key) % 10)
        # any non-digit/non-letter characters in encrypted text
        else:
            plaintext += character

    return plaintext