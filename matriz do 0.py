#criar matriz
entrada=input()
entrada=entrada.split()
L=int(entrada[0])
C=int(entrada[1])
lista=[]
matriz=[]
for i in range(L):
    lista = []
    for j in range(C):
        lista.append(int(input()))
    matriz.append(lista)
print(matriz)
#ordenar matriz
for i in range(L):
    for j in range(C):
        print(matriz[i][j],end=' ')
    print()