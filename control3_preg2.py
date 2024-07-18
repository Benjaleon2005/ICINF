def convierte_negativo(lista):
    return [-num for num in lista]

# Función principal
def main():
    # Pedir al usuario que ingrese 10 números enteros positivos
    numeros = []
    print("Ingrese 10 números enteros positivos:")
    for _ in range(10):
        while True:
            try:
                num = int(input(f"Ingrese el número {_+1}: "))
                if num > 0:
                    numeros.append(num)
                    break
                else:
                    print("Por favor, ingrese un número entero positivo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")
    
    # Convertir la lista de números a negativos
    negativos = convierte_negativo(numeros)
    
    # Mostrar el resultado
    print("Lista original:", numeros)
    print("Lista convertida a negativos:", negativos)

if __name__ == "__main__":
    main()
