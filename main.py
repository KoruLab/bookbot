from collections import Counter

def main(s, w=20):
    with open (f"books/{s.lower()}.txt") as f:      
        file_contents = f.read().lower()
    print(cuenta_palabras(s, file_contents))    
    print(cuenta_letras(s, file_contents))
    print(frecuencia_palabras(s, file_contents, w))

def cuenta_palabras(s, file_contents):
    contador = len(file_contents.split())
    return(f"El número de palabras en {s.capitalize()} es {contador}")
      

def cuenta_letras(s, file_contents):
        contador = dict(Counter(file_contents.lower()).most_common())
        return(f"La frecuencia de letras y símbolos de {s.capitalize()} es {contador}")
def frecuencia_palabras(s, file_contents, w=20):
        contador = dict(Counter(file_contents.lower().split()).most_common(w))
        return(f"Las {w} palabras más usadas en {s.capitalize()} son {contador}")


main("Frankenstein")
    

