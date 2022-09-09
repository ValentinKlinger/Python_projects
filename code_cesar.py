alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
texte = input('What do you want encrypted or decrypted? \n')
key = int(input('key ? (you can put a negative key if you want to encrypt) \n'))

def cesar(texte, key):
    output = ''
    for lettre in texte:
        try:
            if alphabet.index(lettre) + key > 25:

                output += alphabet[alphabet.index(lettre) + key - 26]
        except ValueError:
            output += lettre
        try:
            if alphabet.index(lettre) + key <= 25:
                output += alphabet[alphabet.index(lettre) + key]
        except ValueError:
            pass
    return output

print(cesar(texte, key))
