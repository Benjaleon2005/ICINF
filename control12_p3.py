
words = []
while True:
    word = input("Ingrese una palabra (deje vacío para terminar): ")
    if word == "":
        break
    words.append(word)


min_length = min(len(word) for word in words)


count_min_length = sum(1 for word in words if len(word) == min_length)

print(f"La palabra más corta tiene {min_length} caracteres.")
print(f"Hay {count_min_length} palabras con la menor cantidad de caracteres.")
