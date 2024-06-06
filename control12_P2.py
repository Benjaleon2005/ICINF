nombres=[]
for i in range(7):
    nombre=input("Ingrese los nombres de las personas: ")
    nombres.append(nombre)

nombres_con_a=[]
for nombre in nombres:
    if len(nombre)>0 and nombre[-1]=="a":
        nombres_con_a.append(nombre)

print("Nombres que terminan con a: ")
print(nombres_con_a)