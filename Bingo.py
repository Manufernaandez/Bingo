import random
#num carton
num1 = []
num2 = []
#num tombola
numeros = []
huc = []
huecos = []
#contadores para los cartones
cont1 = 0
cont2 = 0
#dos pares de arrays para crear los numeros del carton, los numeros tombola, los huecos establecidos (el array set) y el numero de huecos respectivamente

for x in range(1, 91):
	numeros.append(x)
    #Lista de los numeros para la tombola, no es importante para el carton
for x in range(1, 9):
    huecos.append(x)
    #IMPORTANTE metodo de creacion de carton por columnas
h1 = random.sample(huecos, 3)
h1.sort()
h2 = random.sample(huecos, 3)
h2.sort()
#Determinar los huecos de los 9 numeros

print(h1)
print(h2)
#comprobacion que los huecos no esten repetidos y esten marcados de comprobacion
for x in range(1,10):
    if x in h1:
        r = random.sample(range(x*10-9, x*10), k=1)
        num1.append(r)
        num1.sort()
    else:
        r = random.sample(range(x*10-9, x*10), k=2)
        r.sort()  
        num1.append(r)
        num1.sort()
#Este for crea en un bucle de 9 los numeros del carton, son arrays dentro de array.
#Si la x es un numero de huc[] solo se introduce un numero en el array, si no;
#lo mismo para carton 2.
for x in range(1,10):
    if x in h2:
        r = random.sample(range(x*10-9, x*10), k=1)
        num2.append(r)
        num2.sort()
    else:
        r = random.sample(range(x*10-9, x*10), k=2)
        r.sort()  
        num2.append(r)
        num2.sort()
#Variable para guardar los numeros que ya han salido
numSalido = []
#pasa num1 por lista1, un array de puros ints para comprobar.
lista1 = []
lista2 = []
while len(lista1) < 15:
    for i in range(0, 9):
        for j in range(0, 2):
            try:
                lista1.append(num1[i][j])
            except:
                pass
#pasa num2 por lista2, un array de puros ints para comprobar.
while len(lista2) < 15:
    for i in range(0, 9):
        for j in range(0, 2):
            try:
                lista2.append(num2[i][j])
            except:
                pass
#creacion de carton1
carton1 = []
#Recorre todo el array de carton1 que está vacío.
for i in range(0, 9):
    for j in range(0, 3):
        try:
            #Si encuentra algo dentro de num1[i][j], pues lo guarda
            carton1.append(num1[i][j])
        except:
            #Si no encuentra nada, le pone un 0, pero mantiene el orden. 
            carton1.append(0)
#Dibujo del carton 1.
carton1Row1 = []
carton1Row2 = []
carton1Row3 = []
#se asignan los valores de graf1 cada uno en una fila, para mostrarlo correctamente. 
for i in range(0, 9):
    carton1Row1.append(carton1[3 * i])
    carton1Row2.append(carton1[3 * i + 1])
    carton1Row3.append(carton1[3 * i + 2])
#creacion de carton2
carton2 = []
#Recorre todo el array de carton1 que está vacío.
for i in range(0, 9):
    for j in range(0, 3):
        try:
            #Si encuentra algo dentro de num1[i][j], pues lo guarda
            carton2.append(num2[i][j])
        except:
            #Si no encuentra nada, le pone un 0, pero mantiene el orden. 
            carton2.append(0)

carton2Row1 = []
carton2Row2 = []
carton2Row3 = []
#se asignan los valores de graf1 cada uno en una fila, para mostrarlo correctamente. 
for i in range(0, 9):
    carton2Row1.append(carton2[3 * i])
    carton2Row2.append(carton2[3 * i + 1])
    carton2Row3.append(carton2[3 * i + 2])


colDe1Cero1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
colDe1Cero2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#quito las posiblidades de tener columnas donde hay 2 0s, por lo que solo quedan columnas con 1 0.
colDe1Cero1.remove(h1[0])
colDe1Cero1.remove(h1[1])
colDe1Cero1.remove(h1[2])
#Lo mismo para el carton 2
colDe1Cero2.remove(h2[0])
colDe1Cero2.remove(h2[1])
colDe1Cero2.remove(h2[2])

#Todos los valores de col1cero están en base 1, pero los pasamos a base 0 para trabajarlo mejor con las posiciones de
#las listas.
colDe1Cero1 = [x - 1 for x in colDe1Cero1]
colDe1Cero2 = [x - 1 for x in colDe1Cero2]


#Todo para carton 1
#En este loop movemos las columnas que tengan 2 0s.
for i in range(1, 10):
    #no hago h[0] porque eso seguira siendo 10-0-0
    #h[1] si es 10-0-0, cambia a 0-10-0
    if i == h1[1]:
        carton1Row2[i - 1] = carton1Row1[i - 1]
        carton1Row1[i - 1] = 0
    #h[2] si es 15-0-0, cambia a 0-0-15 
    if i == h1[2]:
        carton1Row3[i - 1] = carton1Row1[i - 1]
        carton1Row1[i - 1] = 0
#formato 15-17-0 a 15-0-17
for i in range (0, 2):
    carton1Row3[colDe1Cero1[i * 3]] = carton1Row2[colDe1Cero1[i * 3]] 
    carton1Row2[colDe1Cero1[i * 3]] = 0
    #formato 15-17-0, se convierte en 0-15-17
    carton1Row3[colDe1Cero1[(i * 3) + 1]] = carton1Row2[colDe1Cero1[(i * 3) + 1]]
    carton1Row2[colDe1Cero1[(i * 3) + 1]] = carton1Row1[colDe1Cero1[(i * 3) + 1]]
    carton1Row1[colDe1Cero1[(i * 3) + 1]] = 0


#Todo para carton 2
#En este loop movemos las columnas que tengan 2 0s.
for i in range(1, 10):
    #no hago h[0] porque eso seguira siendo 10-0-0
    #h[1] si es 10-0-0, cambia a 0-10-0
    if i == h2[1]:
        carton2Row2[i - 1] = carton2Row1[i - 1]
        carton2Row1[i - 1] = 0
    #h[2] si es 15-0-0, cambia a 0-0-15 
    if i == h2[2]:
        carton2Row3[i - 1] = carton2Row1[i - 1]
        carton2Row1[i - 1] = 0
#formato 15-17-0 a 15-0-17
for i in range (0, 2):
    carton2Row3[colDe1Cero2[i * 3]] = carton2Row2[colDe1Cero2[i * 3]] 
    carton2Row2[colDe1Cero2[i * 3]] = 0
    #formato 15-17-0, se convierte en 0-15-17
    carton2Row3[colDe1Cero2[(i * 3) + 1]] = carton2Row2[colDe1Cero2[(i * 3) + 1]]
    carton2Row2[colDe1Cero2[(i * 3) + 1]] = carton2Row1[colDe1Cero2[(i * 3) + 1]]
    carton2Row1[colDe1Cero2[(i * 3) + 1]] = 0

print("Cartón 1: ")
print(carton1Row1)
print(carton1Row2)
print(carton1Row3)
print("Cartón 2:")
print(carton2Row1)
print(carton2Row2)
print(carton2Row3)


#El juego en sí.
while True:
    bombo = random.choice(numeros)
    if bombo not in numSalido:
        numSalido.append(bombo)
        print("Bombo", bombo)
        #Puede agregarse "numSalido.sort()" para poner los numeros que han salido, en orden.
        print("numsalido", numSalido)
        if cont1 < 15 or cont2 < 15:
            if bombo in lista1:
                cont1 = cont1 + 1
                for i in range(0, 9):
                    if carton1Row1[i] == bombo:
                        carton1Row1[i] = 'X'
                    if carton1Row2[i] == bombo:
                        carton1Row2[i] = 'X'
                    if carton1Row3[i] == bombo:
                        carton1Row3[i] = 'X'    
                print("Carton 1 tiene", cont1, "numero(s) correcto(s) hasta ahora")
            if bombo in lista2:
                cont2 = cont2 + 1
                for i in range(0, 9):
                    if carton2Row1[i] == bombo:
                        carton2Row1[i] = 'X'
                    if carton2Row2[i] == bombo:
                        carton2Row2[i] = 'X'
                    if carton2Row3[i] == bombo:
                        carton2Row3[i] = 'X'
                print("Carton 2 tiene", cont2, "numero(s) correcto(s) hasta ahora")
        if cont1 == 15 and cont2 == 15:
            print("Ambos cartones han ganado el Bingo!")
            print("Los numeros que han salido hasta ahora son:", numSalido)
            print("Cartón 1: ")
            print(carton1Row1)
            print(carton1Row2)
            print(carton1Row3)
            print("Cartón 2:")
            print(carton2Row1)
            print(carton2Row2)
            print(carton2Row3)
            break
        if cont1 == 15:
            print("El ganador es el cartón 1!")
            print("Los numeros que han salido hasta ahora son:", numSalido)
            print("Cartón 1: ")
            print(carton1Row1)
            print(carton1Row2)
            print(carton1Row3)
            print("Cartón 2:")
            print(carton2Row1)
            print(carton2Row2)
            print(carton2Row3)
            break
        if cont2 == 15:
            print("El ganador es el cartón 2!")
            print("Los numeros que han salido hasta ahora son:", numSalido)
            print("Cartón 1: ")
            print(carton1Row1)
            print(carton1Row2)
            print(carton1Row3)
            print("Cartón 2:")
            print(carton2Row1)
            print(carton2Row2)
            print(carton2Row3)
            break