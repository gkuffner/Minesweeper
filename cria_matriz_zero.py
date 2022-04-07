def cria_matriz_zero(dimensao):
    """Cria uma matriz dimensao x dimensao preenchida com zeros (que representa as casas sem bomba); int. → mat."""
    m_final = []
    for a in range(dimensao):  # Adiciona as linhas
        m_temp = []
        for b in range(dimensao):  # Adiciona as colunas
            m_temp.append(0)
        m_final.append(m_temp)
    return m_final
