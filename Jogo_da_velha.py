import os  #biblioteca para apagar o tabuleiro
import random # biblioteca para fazer o sorteio
import time # time  caso a cpu começa para não apagar o tabuleiro
m = [[' ',' ',' '],[' ', ' ',' '],[' ', ' ',' ']]
derrotas = 0
empates = 0
vitorias = 0
def inicio(m): # inicia o jogo
    if (primeiro == 0):
        tabuleiro()
        print(' Jogador Comeca ')
        linha = int(input(' Digite uma linha: '))
        coluna = int(input(' Digite uma coluna: '))
        m[linha - 1][coluna - 1] = 'O'
    elif (primeiro == 1):
        tabuleiro()
        print('CPU Comeca')
        time.sleep(1.5)
        os.system("cls")

    if (m[1][1] == 'O' or m[0][0] == ' ' ):
        m[0][0] = 'X'
    elif (m[0][0] == 'O' or m[1][1] == ' ' ):
        m[1][1] = 'X'


def tabuleiro():  # tabuleiro do jogo
    os.system("cls")
    print('\t')
    print (f' Derrotas == {derrotas}')
    print (f' Vitorias == {vitorias}')
    print (f' Empates == {empates} \n')

    print(f'   {m[0][0]} | {m[0][1]} | {m[0][2]}')
    print(f'  ___|___|___')
    print(f'   {m[1][0]} | {m[1][1]} | {m[1][2]}')
    print(f'  ___|___|___')
    print(f'   {m[2][0]} | {m[2][1]} | {m[2][2]}')


def vitoria (m): # verifica condição de vitótia
    fim = 0
    linhas = [0,0,0]
    colunas = [0,0,0]

    for i in range(3): # calcula número de casas ocupadas pelo X e aloca em um vetor na linha e coluna
        for j in range(3):
            if (m[i][j] == 'X'):
                linhas[i] += 1
                colunas[j] += 1
    for l in range(3):
        for c in range(3): # localiza as posições na linha para a condição de vitória da cpu
            if ( linhas[l] == 2 and m[l][c] == ' ' and fim == 0):
                m[l][c] = 'X'
                fim = 1 # variável que quebra as outras condições
                break
    for a in range(3): # localiza as posições na coluna para a condição de vitória da cpu
        if (fim == 0 and colunas[a] == 2):
            for b in range(3):
                if (m[b][a] == ' '):
                    m[b][a] = 'X'
                    fim = 1
                    break
    if (m[0][0] == m[2][2] == 'X' or m[0][2] == m[2][0] == 'X' and m[1][1] == ' ' and fim == 0):  # condições de vitória pra diagonais
        m[1][1] = 'X'
        fim = 1
    if (m[0][2] == m[1][1] == 'X' and m[2][0] == ' ' and  fim == 0):
        m[2][0] = 'X'
        fim = 1
    if (m[0][0] == m[1][1] == 'X' and m[2][2] == ' ' and fim == 0):
        m[2][2] = 'X'
        fim = 1
    return fim

def  sorteio():   # função pra sortear quem começa primeiro
    sort = random.randint(0,1)
    return sort

def bot(m , vez):  #jogadas do bot
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

    if (vez > 2 and end == 0): # jogadas restantes que não interfere na vitória e nem na derrota
        for cont1 in range(3): # completa as posições restantes na  matri
            for cont2 in range(3):
                if (m[cont1][cont2] == ' ' and end == 0):
                    m[cont1][cont2] = 'X'
                    end = 1
                    break
    return m
  # Programa principal
vencedor = 0
rodada = 1
primeiro = sorteio()
inicio(m)
tabuleiro()
rodada+=1
pos_vitoria = 0
jogar_novamente = ' '

while (vencedor == 0 and rodada < 6 or jogar_novamente != 'n'):
    linha = int(input( ' Digite uma linha: '))
    coluna = int(input( ' Digite uma coluna: '))
    while(m[linha-1][coluna-1] != ' ' ):  # verifica se a posicões estão livres entre 0 e 3
        print(' Jogada Invalida \n')
        linha = int(input(' Digite uma linha: '))
        coluna = int(input(' Digite uma coluna: '))
    tabuleiro()
    m[linha-1][coluna-1] = 'O'

    pos_vitoria = vitoria(m)
    if(pos_vitoria == 0):
        m = bot(m, rodada)
    elif (pos_vitoria == 1):
        vencedor = 2
    rodada+=1
    tabuleiro()
    print (f' Rodada == {rodada}')
    if (rodada == 6 or vencedor != 0):
        if (vencedor == 1):
            print(f' O Vencedor e o Jogador')
            vitorias +=1
        elif(vencedor  == 2):
            print(' CPU Venceu ')
            derrotas +=1 
        else:
            print (' Empate ')
            empates += 1
        jogar_novamente = input('\n Deseja Jogar Novamente {s/n} ?')
    if (jogar_novamente == 's'):
        jogar_novamente = ' '
        m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        rodada = 2
        vencedor = 0
        primeiro = sorteio()
        inicio(m)
        tabuleiro()
