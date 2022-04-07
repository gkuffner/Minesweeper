def cria_mascara(dimensao):
    """Fornece a máscara do campo, com símbolos demonstrando as casas fechadas; int. → mat."""
    # Cria uma matriz dimensao x dimensao preenchida com zeros (que representa as casas sem bomba)
    mask_ini = []
    for a in range(dimensao):  # Adiciona as linhas
        m_temp = []
        for b in range(dimensao):  # Adiciona as colunas
            m_temp.append('?')
        mask_ini.append(m_temp)
    return mask_ini
