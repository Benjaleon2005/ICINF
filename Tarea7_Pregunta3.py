supermercado={}

while True:
    producto=input("Ingrese un producto: ")
    if producto=="":
        break
    cantidad=int(input("Ingrese las cantidades: "))
    supermercado[producto]=cantidad

x=int(input("Ingrese un numero para multiplicar las cantidades: "))

for producto, cantidad in supermercado.items():
    nueva_cantidad=cantidad*x
    print("Producto: ", producto, "Cantidad multiplicada", nueva_cantidad)