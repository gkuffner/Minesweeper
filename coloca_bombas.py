import random
from cria_matriz_zero import cria_matriz_zero


def coloca_bombas(dimensao, n_bombas):
    """Cria uma matriz dimensão x dimensão preenchida com zeros (que representam as casas sem bomba) e
    bombas aleatórias; int. → mat"""
    # Coloca as bombas aleatoriamente na matriz anteriormente criada
    m_final = cria_matriz_zero(dimensao)
    bombas_colocadas = 0
    while bombas_colocadas < n_bombas:
        local = random.randint(0, dimensao**2-1)
        l_bomba = local // dimensao  # Pega a parte inteira da divisao para encontrar em que linha o numero se encontra
        c_bomba = local % dimensao  # Pega o resto da divisao para encontrar a coluna em que o numero se encontra
        if m_final[l_bomba][c_bomba] == "B":  # Se no local já houver uma bomba, volta para criar
            # outra posição ate que não haja bomba nessa posição
            continue
        m_final[l_bomba][c_bomba] = "B"  # Adiciona a bomba na matriz
        bombas_colocadas += 1
    return m_final
