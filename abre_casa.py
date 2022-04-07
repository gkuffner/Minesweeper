from entorno import entorno


def abre_casa(mascara, campo, i, j):
    """Atualiza a máscara para mostrar o conteúdo da casa i, j.
    Se essa casa tiver um zero, mostrar também as casas vizinhas com zero.
    Retorna o número de casas que foi aberta e atualiza a máscara
    mat., mat., int., int. → int. (atualiza a máscara)"""

    mascara[i][j] = campo[i][j]
    abertas = 1
    if campo[i][j] == 0:
        vizinhos = entorno(i, j, len(mascara))
        for casa in vizinhos:
            if campo[casa[0]][casa[1]] == 0 and mascara[casa[0]][casa[1]] != 0:
                abertas += abre_casa(mascara, campo, casa[0], casa[1])
    return abertas
