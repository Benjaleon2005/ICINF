def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

def ingresar_elemento(lista):
    elemento = input("Ingrese el elemento a agregar: ")
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado a la lista.")

def modificar_elemento(lista):
    try:
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice < len(lista):
            nuevo_elemento = input("Ingrese el nuevo valor: ")
            lista[indice] = nuevo_elemento
            print(f"Elemento en el índice {indice} modificado a '{nuevo_elemento}'.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido para el índice.")

def eliminar_elemento(lista):
    try:
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if 0 <= indice < len(lista):
            elemento_eliminado = lista.pop(indice)
            print(f"Elemento '{elemento_eliminado}' en el índice {indice} eliminado.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido para el índice.")

def eliminar_ultimo_elemento(lista):
    if lista:
        elemento_eliminado = lista.pop()
        print(f"Último elemento '{elemento_eliminado}' eliminado de la lista.")
    else:
        print("La lista está vacía, no se puede eliminar el último elemento.")

def buscar_elemento(lista):
    elemento = input("Ingrese el elemento a buscar: ")
    try:
        indice = lista.index(elemento)
        print(f"Elemento '{elemento}' encontrado en el índice {indice}.")
    except ValueError:
        print(f"Elemento '{elemento}' no encontrado en la lista.")

def mostrar_elementos(lista):
    if lista:
        print("Elementos en la lista:")
        for i, elemento in enumerate(lista):
            print(f"{i}: {elemento}")
    else:
        print("La lista está vacía.")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == '1':
            ingresar_elemento(lista)
        elif opcion == '2':
            modificar_elemento(lista)
        elif opcion == '3':
            eliminar_elemento(lista)
        elif opcion == '4':
            eliminar_ultimo_elemento(lista)
        elif opcion == '5':
            buscar_elemento(lista)
        elif opcion == '6':
            mostrar_elementos(lista)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
