words=[]

while True:
    word=input("Ingrese una palabra a la lista: ")
    if word=="":
        break
    words.append(word)

for word in words:
    count_a=0
    for i in range(len(word)):
        if word[i]=="A" or word[i]=="a":
            count_a=count_a+1

print("la palabra", word, "tiene", count_a, "letras A o a.")

    