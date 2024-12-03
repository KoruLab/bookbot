from collections import Counter

def main():
    with open ("books/frankenstein.txt") as f:
        
        file_contents = f.read().split()
        contador = len(file_contents)
    print(contador)


    

main()