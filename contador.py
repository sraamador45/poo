import string

def caractermax(palabra):

    alfabeto = string.ascii_letters
    diccionario = {}

    for letras in alfabeto:
        diccionario[letras] = 0

    for letras in palabra:
        diccionario[letras] += 1

    diccionario = sorted(diccionario.items(), 
                        reverse=True, 
                        key=lambda x: x[1])

    for position in range(0, 26):
        print (diccionario[position])
        if position != len(diccionario) - 1:
            if diccionario[position + 1][1] < diccionario[position][1]:
                break
print("anan caracter maximo")
caractermax("anan")
print("HOla mundo caracter maximo")
h="hola mundo"
h.replace(" ", "")

caractermax(h)