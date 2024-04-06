#Escribe un programa que lea una lista de nombres e imprima la lista en orden alfabético.
lista_nombres=['daniel','juan','pedro','amanda']
lista_ordenada=[]
for i in lista_nombres:
  lista_ordenada.append(i)
  lista_ordenada.sort()
print(lista_ordenada)
