altura=1.0
alturas=0
cant_persona=0
while altura!=0.0:
    altura=float(input("Ingrese altura de la persona: "))
    if altura!=0.0:
        alturas+=altura
        cant_persona+=1
if cant_persona!=0:
    promedio = alturas / cant_persona
    print("La altura promedio es: ", promedio)
