import os
import random
m = [[' ',' ',' '],[' ', ' ',' '],[' ', ' ',' ']]
def inicio(m):
    if (primeiro == 0):
        tabuleiro()
        print(' Jogador Comeca ')
        linha = int(input(' Digite uma linha: '))
        coluna = int(input(' Digite uma coluna: '))
        m[linha - 1][coluna - 1] = 'O'

    if (primeiro == 1):
        print(' CPU Comeca ')

    if (m[1][1] == 'O' or m[0][0] == ' ' ):
        m[0][0] = 'X'
    elif (m[0][0] == 'O' or m[1][1] == ' ' ):
        m[1][1] = 'X'


def tabuleiro():
    print(f'   {m[0][0]} | {m[0][1]} | {m[0][2]}')
    print(f'  ___|___|___')
    print(f'   {m[1][0]} | {m[1][1]} | {m[1][2]}')
    print(f'  ___|___|___')
    print(f'   {m[2][0]} | {m[2][1]} | {m[2][2]}')


def vitoria (m):
    fim = 0
    linhas = [0,0,0]
    colunas = [0,0,0]

    for i in range(3):
        for j in range(3):
            if (m[i][j] == 'X'):
                linhas[i] += 1
                colunas[j] += 1
    for l in range(3):
        for c in range(3):
            if ( linhas[l] == 2 and m[l][c] == ' ' and fim == 0):
                m[l][c] = 'X'
                fim = 1
                break
    for a in range(3):
        if (fim == 0 and colunas[a] == 2):
            for b in range(3):
                if (m[b][a] == ' '):
                    m[b][a] = 'X'
                    fim = 1
                    break
    if (m[0][0] == m[2][2] == 'X' or m[0][2] == m[2][0] == 'X' and m[1][1] == ' ' and fim == 0):
        m[1][1] = 'X'
        fim = 1
    if (m[0][2] == m[1][1] == 'X' and m[2][0] == ' ' and  fim == 0):
        m[2][0] = 'X'
        fim = 1
    if (m[0][0] == m[1][1] == 'X' and m[2][2] == ' ' and fim == 0):
        m[2][2] = 'X'
        fim = 1
    return fim

def  sorteio():
    sort = random.randint(0,1)
    return sort

def bot(m , vez):
    lin = [0,0,0]
    col = [0,0,0]
    end = 0

    if (m[0][2] == m[1][1] == 'O' and m[2][0] == ' ' and end == 0):
        m[2][0] = 'X'
        end = 1
    if (m[0][0] == m[2][2] == 'O' and m[1][1] == 'X' and m[0][1] == ' ' and end == 0):
        m[0][1] = 'X'
        end = 1
    for i in range(3):
        for j in range(3):
            if (m[i][j] == 'O'):
                lin[i] += 1
                col[j] += 1
    for l in range(3):
        for c in range(3):
            if ( lin[l] == 2 and m[l][c] == ' ' and end == 0):
                m[l][c] = 'X'
                end = 1
                break
    for a in range(3):
        if (end == 0 and col[a] == 2):
            for b in range(3):
                if (m[b][a] == ' '):
                    m[b][a] = 'X'
                    end = 1
                    break

    if (m[1][1] == m[2][0] == 'O' and m[0][2] == ' '):
        m[0][2] = 'X'
        end = 1
    if (m[0][1] == m[1][0] == 'O' and m[1][1] == ' '):
        m[1][1] = 'X'
        end = 1
    if (m[0][0] == m[2][2] == 'O' and m[1][1] == ' ' and end == 0):
        m[1][1] = 'X'
        end = 1
    if (m[0][0] == m[0][2] == 'O' and m[0][1] == ' ' and end == 0):
        m[0][1] = 'X'
        end = 1
    if (m[0][0] == m[1][1] == 'O' and m[2][0] == ' ' and end == 0):
        m[2][0] = 'X'
        end = 1
    if (vez == 2 and m[0][2] == ' ' and end == 0): # Caso Especifico
        m[0][2] = 'X'
        end = 1
    elif (vez == 2 and m[0][1] == ' ' and end == 0): # Caso Especifico
        m[0][1] = 'X'
        end = 1

    if (m[0][0] == m[2][2] == 'O' or m[0][2] == m[2][0] == 'O' and m[1][1] == ' ' and end == 0):
        m[1][1] = 'X'
        end = 1
    elif (m[1][1] == m[2][0] == 'O' and m[0][2] == ' ' and end == 0):
        m[0][2] = 'X'
        end = 1
    elif (vez == 2 and m[1][1] == ' ' and end == 0):
        m[1][1] = 'X'
        end = 1
    elif (vez == 2 and m[0][2] == ' ' and end == 0):
        m[0][2] = 'X'
        end = 1
    elif (vez == 2 and m[0][1] == ' ' and end == 0):
        m[0][1] = 'X'
        end = 1

    if (vez > 2 and end == 0):
        for cont1 in range(3):
            for cont2 in range(3):
                if (m[cont1][cont2] == ' ' and end == 0):
                    m[cont1][cont2] = 'X'
                    end = 1
                    break
    return m

vencedor = 0
vez = 1
primeiro = sorteio()
inicio(m)
tabuleiro()
vez+=1
pos_vitoria = 0
jogar_novamente = ' '

while (vencedor == 0 and vez < 6 or jogar_novamente != 'n'):
    linha = int(input( ' Digite uma linha: '))
    coluna = int(input( ' Digite uma coluna: '))
    while(m[linha-1][coluna-1] != ' ' ):
        print(' Jogada Invalida \n')
        linha = int(input(' Digite uma linha: '))
        coluna = int(input(' Digite uma coluna: '))
    tabuleiro()
    m[linha-1][coluna-1] = 'O'

    pos_vitoria = vitoria(m)
    if(pos_vitoria == 0):
        m = bot(m, vez)
    elif (pos_vitoria == 1):
        vencedor = 2

    vez+=1
    tabuleiro()
    print (f' Rodada == {vez}')
    if (vez == 6 or vencedor != 0):
        if (vencedor == 1):
            print(f' O Vencedor e o Jogador')
        elif(vencedor  == 2):
            print(' CPU Venceu ')
        else:
            print (' Empate ')
        jogar_novamente = input('\n Deseja Jogar Novamente {s/n} ?')
    if (jogar_novamente == 's'):
        jogar_novamente = ' '
        m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        vez = 2
        vencedor = 0
        primeiro = sorteio()
        inicio(m)
        tabuleiro()
