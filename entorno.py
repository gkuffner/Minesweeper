def entorno(linha, coluna, dimensao):
    """Retorna uma lista com as coordenadas das casas vizinhas
    int. (x3) → list"""
    linhas = [linha]
    colunas = [coluna]
    if linha > 0:
        linhas = linhas + [linha-1]
    if linha+1 < dimensao:
        linhas = linhas + [linha+1]
    if coluna > 0:
        colunas = colunas + [coluna-1]
    if coluna+1 < dimensao:
        colunas = colunas + [coluna+1]
    vizinhos = []
    for i in linhas:
        for j in colunas:
            vizinhos = vizinhos + [(i, j)]
    vizinhos.remove((linha, coluna))
    return vizinhos
