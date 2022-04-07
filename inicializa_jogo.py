from cria_mascara import cria_mascara
from atualiza_vizinhos import atualiza_vizinhos
from coloca_bombas import coloca_bombas


def inicializa_jogo(dimensao, n_bombas):
    """Usa todas as outras funções e funções de sorteio aleatório. Coloca as minas em posições aleatórias do campo
     inicializado e os números nas casas vizinhas as minas de forma coerente. Não recebe argumentos de entrada porque,
     inicialmente, serão pedidos na execução da função; inicialmente retorna uma matriz"""
    # Pede as dimensões do campo e a quantidade de bombas e converte ambos para int.

    mascara_inicial = cria_mascara(dimensao)  # Cria a máscara inicial com a mesma dimensão do campo

    campo_inicial = coloca_bombas(dimensao, n_bombas)
    atualiza_vizinhos(campo_inicial, dimensao)
    return campo_inicial, mascara_inicial
