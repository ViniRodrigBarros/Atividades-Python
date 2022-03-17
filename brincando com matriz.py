matriz=[]
lista1=[]
lista2=[]
lista3=[]
listamedia=[]
listapositivo=[]
listamedia2=[]
matrizsemdiagonal=[]
num=0
num1=0
for i in range(3):
    num=float(input())
    lista1.append(num)
    listamedia.append(num)

for i in range(3):
    num=float(input())
    lista2.append(num)
    listamedia.append(num)
for i in range(3):
    num=float(input())
    lista3.append(num)
    listamedia.append(num)
matriz.append(lista1)
matriz.append(lista2)
matriz.append(lista3)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=' ')
    print('\n')
for i in range(9):
    if listamedia[i] > 0:
        x=listamedia[i]
        listapositivo.append(x)
media=(sum(listapositivo)/len(listapositivo))

listamedia2 = listamedia
listamedia2.sort()

menor=listamedia2[0]

matrizsemdiagonal=listamedia

matrizsemdiagonal.pop(0)
matrizsemdiagonal.pop(3)
matrizsemdiagonal.pop(6)

somadiagonal=sum(matrizsemdiagonal)

delta=''
if (menor % 2) == 0:
    delta=1
else:
    delta=0

print('{:.2f} {:.0f} {:.0f} {:.0f}'.format(media,menor,delta,somadiagonal))