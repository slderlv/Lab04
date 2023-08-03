import numpy as np
# Ejercicios

# Generar una lista de 100 números de forma aleatoria con números enteros entre 1 y 10
lista = []
for _ in range(100):
  lista.append(np.random.randint(1, 11))
print(lista)

# Agregarlos a un diccionario
tempDictionary = {}

for number in lista:
  if number in tempDictionary:
    tempDictionary[number] += 1
  else:
    tempDictionary[number] = 1

# Ordenar el diccionario por claves
frequencyDictionary = dict(sorted(tempDictionary.items()))

# Determinar números con máxima y mínima frecuencia
highestFrequency = []
lowestFrequency = []

for num, freq in frequencyDictionary.items():
  print("Número",str(num)+":",freq,"veces")
  
  if(freq == max(frequencyDictionary.values())):
    highestFrequency.append(num)
  
  if(freq == min(frequencyDictionary.values())):
    lowestFrequency.append(num)

print("Número(s) que más se repite(n):",highestFrequency,"con un recuento de",max(frequencyDictionary.values()),"oportunidades")
print("Número(s) que menos se repite(n):",lowestFrequency,"con un recuento de",min(frequencyDictionary.values()),"oportunidades")