def main():
    notas = []

    while True:
        nota = float(input("Ingrese una nota : "))
        if nota == 0:
            break
        notas.append(nota)

    if notas:
        cantidad_notas = len(notas)
        promedio_notas = sum(notas) / cantidad_notas
        nota_minima = min(notas)
        nota_maxima = max(notas)

        print(f"Cantidad de notas: {cantidad_notas}")
        print(f"Promedio de notas: {promedio_notas:.2f}")
        print(f"Nota mínima: {nota_minima}")
        print(f"Nota máxima: {nota_maxima}")
    else:
        print("No se ingresaron notas.")

if __name__ == "__main__":
    main()
