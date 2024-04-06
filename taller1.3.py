#3.	Escribe un programa que lea una lista de palabras e imprima la lista de palabras
# que comiencen con una determinada letra.
palabra = []
Lista_palabras = ["burro","vaca","carro","casa"]
lista = [Lista_palabras]
lista.append(palabra)
x = input("ingresar letra:")
for palabra in Lista_palabras:
    if palabra[0] == x :
       print(palabra)
