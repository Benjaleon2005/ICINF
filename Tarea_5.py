total_preguntas=int(input("Ingrese el total de preguntas que se realizaron: "))
preguntas_correctas=int(input("Ingrese la cantidad de preguntas que contesto correctamente: "))

porcentaje_correctas=(preguntas_correctas / total_preguntas) * 100

if porcentaje_correctas>=95:
    nivel="Nivel maximo"
else:
    if porcentaje_correctas>=70:
        nivel="Nivel medio"
    else:
        if porcentaje_correctas>=40:
            nivel="Nivel regular"
        else:
            nivel="Fuera de nivel"

print("El porcentaje de respuestas correctas es: ", porcentaje_correctas, "%")
print("El nivel del postulantes es: ", nivel)
        