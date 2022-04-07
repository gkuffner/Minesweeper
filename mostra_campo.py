def mostra_campo(matriz_situacao):
    """Apresenta a situacao do jogo para o usuário. Recebe a matriz a ser mostrada e nao retorna nada, apenas imprime
    a matriz atual com formatação em quadrado. USADO APENAS PARA FORMATAÇÃO DA MATRIZ."""
                                # Modela a matriz aos padrões em que estamos acostumados
    i = len(matriz_situacao)
    for a in range(i):
        for b in range(i):
            print(matriz_situacao[a][b], end=' | ')
        print()
