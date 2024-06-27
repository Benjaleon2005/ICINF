paises_capitales = {}

print("Ingrese 5 países y sus respectivas capitales:")
for _ in range(5):
    pais = input("Ingrese el nombre del país: ")
    capital = input("Ingrese el nombre de la capital: ")
    paises_capitales[pais] = capital

nombre_turista = input("Ingrese el nombre del turista: ")
pais_procedencia = input("Ingrese el país de procedencia del turista: ")

if pais_procedencia in paises_capitales:
    capital_procedencia = paises_capitales[pais_procedencia]
    print(f"{nombre_turista} es un turista que proviene de {pais_procedencia}, cuya capital es {capital_procedencia}.")
else:
    print(f"El país {pais_procedencia} no está en la lista de países ingresados.")
