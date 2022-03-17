p1=''
p2=''
contp1 = 0
contp2 = 0
print("Insira o nome do player 1")
player1=input()
print("Insira o nome do player 2")
player2=input()

for i in range(5):
    print(player1)
    p1 = input().upper()
    if (p1 != 'PAPEL' and p1 != 'PEDRA' and p1 != 'TESOURA'):
        print("Erro \n opção invalida")
        exit()
    print(player2)
    p2 = input().upper()
    if (p2 != 'PAPEL' and p2 != 'PEDRA' and p2 != 'TESOURA'):
        print("Erro \n opção invalida")
        exit()
    if (p1 == 'PAPEL' and p2 == 'PEDRA') or (p1 == 'PEDRA' and p2 == 'TESOURA') or (p1 == 'TESOURA' and p2 == 'PAPEL'):
        contp1 += 1
    elif (p2 == 'PAPEL' and p1 == 'PEDRA') or (p2 == 'PEDRA' and p1 == 'TESOURA') or (
            p2 == 'TESOURA' and p1 == 'PAPEL'):
        contp2 += 1

if contp1 > contp2 :
    print('vitoria')
    print(player1)
elif contp1 < contp2:
    print('vitoria')
    print(player2)
elif contp1 == contp2:
    print('empate')