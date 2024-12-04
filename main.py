from collections import Counter

def main(s, w=20):
    with open (f"books/{s.lower()}.txt") as f:      
        file_contents = f.read().lower()
    #print(cuenta_palabras(s, file_contents))    
    #print(cuenta_letras(s, file_contents))
    #print(frecuencia_palabras(s, file_contents, w))
    return(report(s, cuenta_palabras(s, file_contents), cuenta_letras(s, file_contents), frecuencia_palabras(s, file_contents, w), w))

def report(s, p, l, f, w):
    print(f"****Análisis de {s.capitalize()}: Número de palabras, frecuencia de letras y frecuencia de palabras****")
    print("1)")
    print(f"La versión del libro estudiada contiene {p} palabras.")
    print("2)")
    print("En cuanto a la frecuencia de las distintas letras en la obra:")
    for i, k in l.items():
        if i == " ":
            pass
        elif i in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, w, x, y, z":
            print(f'La "{i}" aparece {k} veces')
    print("3)")
    
    for i, k in f.items():
        if w == 1:
            print(f"Por último, la palabra más frecuente es {i} que aparece {k} veces")
        elif w > 0:
            print(f"Por último, y en cuanto a las {w} palabras más frecuentes:")
            print(f'-"{i.capitalize()}" aparece {k} veces')
    print("")
    print("Gracias por usar este analizador de textos. Recuerda que puedes analizar cualquier texto en /books")
      

def cuenta_palabras(s, file_contents):
    contador = len(file_contents.split())
    return contador
      

def cuenta_letras(s, file_contents):
    letras = dict(Counter(file_contents.lower()).most_common())
    return(letras)
def frecuencia_palabras(s, file_contents, w=20):
    contador = dict(Counter(file_contents.lower().split()).most_common(w))
    return(contador)


main("Frankenstein", 23)
    

