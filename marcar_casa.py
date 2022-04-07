def marcar_casa(mascara, linha, coluna):
    """Coloca um símbolo na casa escolhida para indicar para nao abrir. Apenas altera a máscara e nao retorna nada;
     mat.[int.]"""
    mascara[linha][coluna] = "X"  # Sinaliza a casa
