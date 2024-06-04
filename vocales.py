def contar_vocales_consonantes(palabra):
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    num_vocales = 0
    num_consonantes = 0
    
    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
    
    return num_vocales, num_consonantes

def main():
    palabras = []
    
    print("Introduce palabras (deja en blanco y presiona Enter para finalizar):")
    while True:
        palabra = input()
        if palabra == "":
            break
        palabras.append(palabra)
    
    for palabra in palabras:
        vocales, consonantes = contar_vocales_consonantes(palabra)
        print(f"Palabra: {palabra}, Vocales: {vocales}, Consonantes: {consonantes}")

if __name__ == "__main__":
    main()
