sueldos_500k_900k=0
sueldos_mas_900k=0
gasto_total=0

sueldo=int(input("Ingrese el sueldo del empleado (ingrese -1 para finalizar): "))

while sueldo!=-1:
    if 500000<=sueldo<=1500000:
        gasto_total+=sueldo
        if sueldo<=900000:
            sueldos_500k_900k+=1
        if sueldo>900000:
            sueldos_mas_900k+=1
    else:
        print("El sueldo debe estar entre $500.000 y $1.500.000")

    sueldo=int(input("Ingrese el sueldo del empleado (ingrese -1 para finalizar)": ))

print("Cantidad de empleados que cobran entre $500.000 y $900.000: ", (sueldos_500k_900k))
print("Cantidad de empleados que cobran mas de $900.000: ", (sueldos_mas_900k))
print("Gasto total de la empresa en sueldos: $", (gasto_total))


