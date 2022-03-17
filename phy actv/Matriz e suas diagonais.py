
entrada=int(input())
lista=[]
matriz=[]
diagonal=[]
num=0
for i in range(entrada):
    lista = []
    for j in range(entrada):
        num+=1
        lista.append(num)
    matriz.append(lista)

#ordenar matriz
for i in range(entrada):
    for j in range(entrada):
        print(matriz[i][j],end=' ')
    print()
print('Diagonal Principal:')
for i in range(entrada):
    for j in range(entrada):
        if i == j:
            print(matriz[i][j], end=' ')
        else:
            print(' ', end='')
    print('\n')
print('Diagonal Secundaria:')

for i in range(entrada):
    for j in range(entrada):
        if (i + j)== (entrada-1):
            print(matriz[i][j], end=' ')
        else:
            print(' ', end='')
    print('\n')