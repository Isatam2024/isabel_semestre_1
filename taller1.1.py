#1. Pide al usuario que ingrese una palabra o frase y usa un ciclo for para contar cuántas vocales (a, e, i, o, u) contiene.
# Luego, muestra el conteo de cada vocal por separado
Frase = str(input("Ingrese una palabra o frase:"))
vocales = ["a", "e", "i", "o","u"]
contador = 0
for vocal in Frase:
    if vocal in vocales:
        contador += 1
print(contador)
