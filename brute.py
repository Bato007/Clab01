from itertools import product
from encryption import Ccesar, Dafin, Dviginere
from inciso2 import metrics
from pprint import pprint

spanish = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
alphabet = {i: spanish.index(i) for i in spanish}
length = len(alphabet)


def bruteCesar(text):
    keys = {}
    for key in range(length):
        decrypted = Ccesar(text, key)   # Se decripta
        error = metrics(decrypted)      # Se obtiene el error
        keys[key] = error               # Se guarda

    pprint(keys)
    decrypted = Ccesar(text, 8)
    print(decrypted)
    # Se obtienen top 5 de llaves
    k_proposal = list(keys.keys())[:5]
    # for key in k_proposal:
    #     decrypted = Dcesar(text, key)
    #     print(decrypted)
    #     input(('Llave:', key, 'Enter'))


def bruteAfin(text):
    results = {}

    for i in range(length):
        if ((i % 3) == 0):
            continue

        for j in range(length):
            decrypted = Dafin(i, j, text)
            error = metrics(decrypted)
            results[(i, j)] = error

    keys = dict(sorted(results.items(), key=lambda item: item[1]))
    k_proposal = list(keys.keys())[:5]
    print(k_proposal)
    for key in k_proposal:
        # decrypted = Dafin(key[0], key[1], text)
        print(results[key])
        input(('Llave:', key, 'Enter'))


def bruteViginere(text):
    options = {}
    for i in range(1, 3):
        combinations = [''.join(j) for j in product(spanish, repeat=i)]
        for k in combinations:
            decrypted = Dviginere(k, text)
            error = metrics(decrypted)      # Se obtiene el error

            # Se compara con el top 50
        print(combinations)


f = open('cipher1.txt', 'r')
cipher = f.read()
bruteCesar(cipher)
