def solo_numeros(var):
    # Verificar que la cadena no esté vacía
    if len(var) == 0:
        return False
    
    # Verificar cada carácter en la cadena
    for char in var:
        if char < '0' or char > '9':
            return False
    
    return True

# Ejemplos de uso
print(solo_numeros("12345"))  # Devuelve True
print(solo_numeros("123a5"))  # Devuelve False
print(solo_numeros(""))       # Devuelve False
print(solo_numeros("00000"))  # Devuelve True
