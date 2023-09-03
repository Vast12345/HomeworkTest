lista = ["hello", 2, True, 2.22]

print(lista)

for palabra in lista:
    print (palabra)


print("---------------------------------------------------------------")
lista.append("Perro")

for word in lista:
    print (word)

print("---------------------------------------------------------------------")

    
new_append = input("What would you like to add to the list: ")

add_new_append = lista.append(new_append)
for word in lista:
    print(word)





