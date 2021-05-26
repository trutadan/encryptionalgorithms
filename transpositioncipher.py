import math

def transposition_encrypt(key, text):
    ciphertext = [''] * key
    # loop through every column in the given text
    for column in range(key):
        pointer = column
        # stops when pointer goes past the length of the message
        while pointer < len(text):
            # place the character at pointer in message at the end of the current column
            ciphertext[column] += text[pointer]
            # move pointer over
            pointer += key
    return ''.join(ciphertext)


def transposition_decrypt(key, text):
    # the function will simulate the columns and rows of the grid that the plaintext is written on
    column_number = int(math.ceil(len(text) / float(key)))

    # the number of rows in our grid
    rows_number = key

    # the number of shaded boxes in the last column of the grid
    shadedBoxes_number = (column_number * rows_number) - len(text)

    # each string in plaintext represents a column in the grid
    plaintext = [''] * column_number
    column = 0
    row = 0
    for symbol in text:
        plaintext[column] += symbol
        column += 1
        # if there are no more columns OR we're at a shaded box, go back to the first column and the next row
        if (column == column_number) or (column == column_number - 1 and row >= rows_number - shadedBoxes_number):
            column = 0
            row += 1
    return ''.join(plaintext)