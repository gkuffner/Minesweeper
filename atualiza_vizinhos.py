from entorno import entorno


def atualiza_vizinhos(campo, dimensao):
    """Bota os números de bombas vizinhas nas casas que não tem bomba
    mat., int. → (não tem retorno, atualiza o campo)"""
    for i in range(dimensao):
        for j in range(dimensao):
            if campo[i][j] != 'B':
                casas_vizinhas = entorno(i, j, dimensao)
                for casa in casas_vizinhas:
                    if campo[casa[0]][casa[1]] == 'B':
                        campo[i][j] = campo[i][j] + 1
    # Não retorna nada
