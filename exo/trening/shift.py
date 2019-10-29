def encrypt(string, shift=1):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    encryptString = ""
    for c in string:
        index = alphabets.index(c)
        encryptString += alphabets[(index + shift) % len(alphabets)]
    return encryptString


def decrypt(encryptString, shift=1):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for c in encryptString:
        index = alphabets.index(c)
        string += alphabets[(index - shift) % len(alphabets)]
    return string


var = "helloworld"
print(encrypt(var))
print(decrypt(encrypt(var)))
