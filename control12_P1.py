lista=[]
for dia in range(1, 16):
    puntaje=int(input("Ingrese los puntajes del alumno: "))
    lista.append(puntaje)

dias_mayor_igual_60=[]
dias_menor_60=[]

for i in range(15):
    if lista[i] >= 60:
        dias_mayor_igual_60.append(f"día {i+1}")
    else:
        dias_menor_60.append(f"día {i+1}")

print("\nDías con puntaje mayor o igual a 60:")
if dias_mayor_igual_60:
    print(", ".join(dias_mayor_igual_60))
else:
    print("Ningún día tuvo un puntaje mayor o igual a 60.")

print("\nDías con puntaje menor a 60:")
if dias_menor_60:
    print(", ".join(dias_menor_60))
else:
    print("Ningún día tuvo un puntaje menor a 60.")