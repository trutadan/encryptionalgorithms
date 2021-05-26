import sys, random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def gcd(x, y):
    # return the GCD of a and b, using Euclid's Algorithm
    while x != 0:
        x, y = y % x, x
    return y


def findModInverse(x, m):
    # returns the modular inverse of a % m,
    # which is the number x such that a * x % m = 1
    if gcd(x, m) != 1:
        return None
        # no mod inverse if a & m aren't relatively prime

    # calculate using the Extended Euclidean Algorithm
    number1, number2, number3 = 1, 0, x
    value1, value2, value3 = 0, 1, m
    while value3 != 0:
        extent = number3 // value3
        value1, value2, value3, number1, number2, number3 = \
            (number1 - extent * value1), (number2 - extent * value2), \
            (number3 - extent * value3), value1, value2, value3
    return number1 % m


def getKeyParts(key):
    firstKey = key // len(SYMBOLS)
    secondKey = key % len(SYMBOLS)
    return (firstKey, secondKey)


def checkKeys(firstKey, secondKey):
    if firstKey == 1:
        sys.exit()
    if secondKey == 0:
        sys.exit()
    if firstKey < 0 or secondKey < 0 or secondKey > len(SYMBOLS) - 1:
        sys.exit()
    if gcd(firstKey, len(SYMBOLS)) != 1:
        sys.exit()


def affine_encrypt(key, text):
    firstKey, secondKey = getKeyParts(key)
    checkKeys(firstKey, secondKey)
    ciphertext = ''
    for symbol in text:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * firstKey + secondKey) % len(SYMBOLS)]
        else:
            ciphertext += symbol
            # just append this symbol unencrypted
    return ciphertext


def getRandomKey():
    while True:
        firstKey = random.randint(2, len(SYMBOLS))
        secondKey = random.randint(2, len(SYMBOLS))
        if gcd(firstKey, len(SYMBOLS)) == 1:
            return firstKey * len(SYMBOLS) + secondKey