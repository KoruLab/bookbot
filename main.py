from collections import Counter

def main(s):
    with open (s) as f:
        
        file_contents = f.read().split()
        contador = len(file_contents)
    print(f"El número de palabras es {contador}")
    print(cuenta_letras(s))

def cuenta_letras(st):
    with open (st) as f:
        file_contents = f.read().lower()
        contador = dict(Counter(file_contents).most_common())
        #return(f"la frecuencia de letras es {letras}")
        return(f"La frecuencia de letras y símbolos es {contador}")


main("books/frankenstein.txt")
    

