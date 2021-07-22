from collections import Counter
from encryption import Ccesar
spanish = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def letterFreq(word):
    word = word.upper()  # Lo pasamos a mayusculas
    # Obtenemos la cantidad de veces que aparece cada letra
    freq = Counter(word)
    prob = {}  # Probabilidades de cada letra

    for key in freq:
        prob[key] = freq[key]/len(word)  # Calculo las probabilidades

    for letter in spanish:  # Por cada letra del diccionario
        if letter not in freq:  # Si no existe la letra
            prob[letter] = 0  # La inicializamos con cero

    # Retormanos el diccionario de probabilidaes ordenado
    return dict(sorted(prob.items()))


def metrics(word):
    spanishFreq = {'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
                   'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
                   'M': 3.15, 'N': 6.71, 'O': 8.68, 'P': 2.51, 'Q': 0.88, 'R': 6.87,
                   'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01, 'X': 0.22,
                   'Y': 0.90, 'Z': 0.52, 'Ñ': 0.31}
    probWord = letterFreq(word)
    comparacion = {}

    for key in spanishFreq:
        spanishFreq[key] = spanishFreq[key]/100  # Probabilidad

    for i in range(len(spanishFreq)):
        keyActual = list(spanishFreq)[i]
        errorabs = abs(spanishFreq[keyActual]-probWord[keyActual])
        comparacion[keyActual] = errorabs/spanishFreq[keyActual]

    sum = 0
    for key in comparacion:
        sum += comparacion[key]

    # Retorno la suma de todos los errores
    return sum
