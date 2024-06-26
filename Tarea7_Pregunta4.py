deudores={}

print("Ingrese los datos de 5 deudores")
for _ in range(5):
    rut=input("Ingrese el RUT de cada deudor: ")
    deuda=float(input("Ingrese la deuda en pesos de cada uno: "))
    deudores[rut]=deuda

while True:
    rut_abono=input("Ingrese el RUT de la persona a abonar (ENTER para finalizar): ")
    if rut_abono=="":
        break
    if rut_abono in deudores:
        abono=float(input("Ingrese el monto del abono: "))
        deudores[rut_abono]-=abono
        if deudores[rut_abono]<=0:
            del deudores[rut_abono]
            print("La deuda de ", rut_abono, "ha sido pagada y de ha eliminado del registro.")
    else:
        print("El RUT ingresado no esta en la lista de deudores.")

print("Personas que quedaron deudoras y sus respectivos saldos de deuda: ")
for rut, deuda in deudores.items():
    print("RUT ", rut, "Deuda", deuda)