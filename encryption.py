# Se obtiene el array del lenguaje
spanish = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
alphabet = [i for i in spanish]

l_association = {i: alphabet.index(i) for i in alphabet}
n_association = {alphabet.index(i): i for i in alphabet}


def mod_inv(x, y):  # Funcion que calcula el inverso modular
    for i in range(y):
        if (x*i) % y == 1:
            return i  # Se retorna


def clean(text):    # Funcion que convierte a mayuscula y quita tildes
    cleaned = text.upper()
    cleaned = cleaned.replace(' ', '')
    return cleaned


def Cafin(a, b, text):  # Cifrado afin, se le manda la llave y el texto
    text = clean(text)
    cripted_text = ''
    length = len(alphabet)

    for letter in text:  # Se obtiene la letra
        x = l_association.get(letter)

        # Si no esta en el alfabeto
        if (x is None):
            cripted_text += letter
        else:
            # Se traslada
            x = (a*x + b) % length
            cripted_letter = n_association.get(x)
            cripted_text += cripted_letter

    return cripted_text


def Dafin(a, b, text):  # Descifrado afin, se le manda la llave y el texto
    plain_text = ''
    text = clean(text)
    for letter in text:  # Se obtiene la letra
        x = l_association.get(letter)

        # Si no esta en el alfabeto
        if (x is None):
            plain_text += letter
        else:
            length = len(alphabet)
            inv = mod_inv(a, length)  # Se calcula el inverso
            x = abs(inv*(x - b)) % length
            plain_letter = n_association.get(x)
            plain_text += plain_letter

    return plain_text


def Ccesar(text, k=None):  # Cifrado cesar se le manda el texto
    return Cafin(1, k or 3, text)


def Dcesar(text, k=None):   # Descifrado cesar se le manda el texto
    return Dafin(1, k or 3, text)


def Cviginere(key, text):  # Cifrado viginere se le manda la llave y texto
    cripted_text = ''
    index = 0
    length = len(alphabet)
    text = clean(text)
    key = clean(key)
    for letter in text:  # Por cada letra
        x = l_association.get(letter)       # Se obtiene el valor de la letra
        k = l_association.get(key[index])   # Se obtiene el valor de la k

        if ((x is None) or (k is None)):
            cripted_text += letter
        else:
            new = (x + k) % length  # Se convierte el indice
            cripted_letter = n_association.get(new)  # Se obtiene la letra
            cripted_text += cripted_letter
        index = (index + 1) % len(key)
    return cripted_text


def Dviginere(key, text):  # Cifrado viginere se le manda la llave y texto
    cripted_text = ''
    index = 0
    length = len(alphabet)
    text = clean(text)
    key = clean(key)
    for letter in text:  # Por cada letra
        x = l_association.get(letter)       # Se obtiene el valor de la letra
        k = l_association.get(key[index])   # Se obtiene el valor de la k
        if ((x is None) or (k is None)):
            cripted_text += letter
        else:

            if (x - k) >= 0:
                new = (x - k) % length  # Se convierte el indice
            else:
                new = (x - k + length) % length
            cripted_letter = n_association.get(new)  # Se obtiene la letra
            cripted_text += cripted_letter
        index = (index + 1) % len(key)
    return cripted_text
