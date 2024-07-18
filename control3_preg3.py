def potencia(num, exp):
    
    if exp == 0:
        return 1
    
    elif exp < 0:
        return 1 / potencia(num, -exp)
    
    else:
        return num * potencia(num, exp - 1)


print(potencia(2, 3))   

