def main():
    precios_dolares = []
    tasa_cambio = 950  # Valor USD/CLP

    print("Ingrese 10 precios de productos en dólares:")
    for _ in range(10):
        precio = float(input("Ingrese el precio en dólares: "))
        precios_dolares.append(precio)

    precios_pesos = [precio * tasa_cambio for precio in precios_dolares]

    print("Lista de precios en pesos chilenos:")
    for precio in precios_pesos:
        print(f"${precio:.2f}")

if __name__ == "__main__":
    main()
