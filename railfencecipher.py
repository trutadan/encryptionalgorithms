def railfence_encrypt(text, key):
    cycle = key * 2 - 2
    ciphertext = ""

    for row in range(key):
        index = 0
        # the first rail
        if row == 0:
            while index < len(text):
                ciphertext += text[index]
                index += cycle

        # the last rail
        elif row == key - 1:
            index = row
            while index < len(text):
                ciphertext += text[index]
                index += cycle

        # the intermediate rails
        else:
            left_index = row
            right_index = cycle - row
            while left_index < len(text):
                ciphertext += text[left_index]

                if right_index < len(text):
                    ciphertext += text[right_index]

                left_index += cycle
                right_index += cycle

    return ciphertext

def railfence_decrypt(text, key):
    cycle = key * 2 - 2
    length = len(text)

    plaintext = "." * length

    cycle = 2 * key - 2
    units = length // cycle

    rail_lengths = [0] * key

    # top rail length
    rail_lengths[0] = units

    # intermediate rail length
    for i in range(1, key - 1):
        rail_lengths[i] = 2 * units

    # bottom rail length
    rail_lengths[key - 1] = 2 * units

    for i in range(length % cycle):
        if i < key:
            rail_lengths[i] += 1
        else:
            rail_lengths[cycle-i] += 1

    # replace characters in the top rail fence
    index = 0
    rail_offset = 0
    for c in text[:rail_lengths[0]]:
        plaintext = plaintext[:index] + c + plaintext[index+1:]
        index += cycle

    rail_offset += rail_lengths[0]

    # replace characters in the intermediate rail fences
    for row in range(1, key - 1):
        left_index = row
        right_index = cycle - row
        left_char = True
        for c in text[rail_offset:rail_offset+rail_lengths[row]]:
            if left_char:
                plaintext = plaintext[:left_index] + c + plaintext[left_index+1:]
                left_index += cycle
                left_char = not left_char
            else:
                plaintext = plaintext[:right_index] + c + plaintext[right_index+1:]
                right_index += cycle
                left_char = not left_char

        rail_offset += rail_lengths[row]

    # replace characters in the bottom rail fence
    index = key - 1
    for c in text[rail_offset]:
        plaintext = plaintext[:index] + c + plaintext[index + 1:]
        index += cycle

    return plaintext