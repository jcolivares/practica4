#!/usr/bin/python3

#Programa que permite leer una lista de datos y manejarse como un cojunto...

print("¿Deseas introducir la lista de números manualmente [Y/n]?", end="")
opcion = input()

opcion = opcion.lower()

if (opcion!= 'y'):
	opcion = 'n'

if(opcion== "y"):
	print("Dame el listado de numerados separados por una coma ',' Ejemplo: 1,2,5,7?", end="")
	lista = input()
	
	#lista = [elemento for l in lista.split(",") if elemento: int(elemento)]

	lista = lista.split(',')
	
	""" --Primer alternativa
	lista2 = list()
	for elemento in lista:
		lista2.append(int(elemento))
	
	print(lista2)
	"""

	"""
	#Segunda alternativa
	indice = 0
	tamLista = len(lista)

	while indice < tamLista:
		lista[indice] = int(lista[indice])
		indice += 1

	print(lista)
	"""

	
	#Tercera alternativa
	for indice, elemento in enumerate(lista):
		lista[indice] = int(elemento)


	print(lista)

else:
	print("Dame el rango de valores (lim inferior, limite superior) (1,7)?")
	