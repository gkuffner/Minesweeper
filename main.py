from abre_casa import abre_casa
import atualiza_vizinhos
import coloca_bombas
import cria_mascara
import cria_matriz_zero
import entorno
from inicializa_jogo import inicializa_jogo
from marcar_casa import marcar_casa
from mostra_campo import mostra_campo
import math
import random


def main():
    """Executa todas as outras funções para jogar o jogo"""

    # Pede a dificuldade, com as dimensoes do campo e o número de bombas ja determinados, e cria o campo e a máscara

    escolha = input("Escolha o nível de dificuldade:\n1: Fácil, matriz 10x10 e 10 minas "
                    "\n2: Médio, matriz 15x15 e 40 minas \n3: Difícil, matriz 22x22 e 99 minas "
                    "\nSua escolha: ")
    escolha = int(escolha)
    if escolha == 1:  # Modo facil
        d = 10
        b = 10

    elif escolha == 2:  # Modo medio
        d = 15
        b = 40

    elif escolha == 3:  # Modo dificil
        d = 22
        b = 99

    dimensao = d
    n_bombas = b
    cam_e_masc = inicializa_jogo(dimensao, n_bombas)
    campo = cam_e_masc[0]
    mascara = cam_e_masc[1]

    # O jogo em si

    casas_reveladas = 0
    casas_vazias = dimensao ** 2 - n_bombas
    while casas_reveladas < casas_vazias:
        mostra_campo(mascara)
        print("Digite suas ações:")
        acao = input("Deseja sinalizar ou cavar a casa? (0 para sinalizar, 1 para cavar): ")
        acao = int(acao)
        linha = input(str.format("Digite a linha da casa (de 1 a {}): ", dimensao))
        linha = int(linha) - 1
        coluna = input(str.format("Digite a coluna da casa (de 1 a {}): ", dimensao))
        coluna = int(coluna) - 1
        if acao == 0:  # Situações ao sinalizar
            if linha + 1 > dimensao or coluna + 1 > dimensao:  # Caso o valor digitado seja maior que o lado da matriz
                print("Valor inválido, tente novamente")
                continue
            else:
                marcar_casa(mascara, linha, coluna)  # Marcar efetivamente a casa
        elif acao == 1:  # Situações ao cavar
            if linha + 1 > dimensao or coluna + 1 > dimensao:  # Caso o valor digitado seja maior que o lado da matriz
                print("Valor inválido, tente novamente")
                continue
            elif campo[linha][coluna] == "B":  # Caso atinja uma bomba, mostra a tela de fim de jogo, bem como o campo
                print("BOMBA! D:")  # Também fornece uma opção rapida para jogar novamente
                print("Mais sorte da próxima vez!")
                mostra_campo(campo)
                z = int(input("Gostaria de jogar novamente? 1 = Sim; 0 = Não: "))
                if z == 1:
                    main()
                elif z == 0:
                    print("Até mais!")
                    break
            elif mascara[linha][coluna] != "?" and mascara[linha][coluna] != "X":
                print("Essa casa já foi aberta, tente novamente")  # Mensagem e ação caso a casa já tenha sido aberta
                continue  # "Continue" faz com que o loop while continue, mas que volte ao começo, pedindo o input
            elif campo[linha][coluna] != "B" and campo[linha][coluna] != "X":  # Ação caso a casa não tenha sido aberta
                casas_reveladas += abre_casa(mascara, campo, linha, coluna)  # Não contabiliza caso o usuario
                # tenha marcado uma casa errada e queira abri-la
            if casas_reveladas == casas_vazias:
                print("Parabéns! Você finalizou o jogo com sucesso! :D")
                z = int(input("Gostaria de jogar novamente? 1 = Sim; 0 = Não: "))  # Mensagem de término com sucesso
                # da partida com opção rapida para começar outra partida
                if z == 1:
                    main()
                elif z == 0:
                    print("Até mais!")
                    break


if __name__ == '__main__':
    main()
