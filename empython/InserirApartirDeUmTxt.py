import math

def ler_grafo_de_arquivo(nome_arquivo):
    """
    Lê a matriz de adjacência de um arquivo TXT.
    
    O arquivo deve conter linhas como:
      0, 2, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0,
      1, 3, 0, 0, 0, 0,
      2, 0, 2, 0, 0, 0,
      0, 0, 10, 5, 0, 4,
      5, 0, 0, 1, 0, 0,
      
    Retorna a matriz (lista de listas) com valores numéricos. Valores 0 fora da diagonal
    serão convertidos para math.inf, representando ausência de conexão.
    """
    INF = math.inf
    matriz = []
    
    try:
        with open(nome_arquivo, 'r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado!")
        exit()
    
    # Processa cada linha removendo espaços e a vírgula final, se houver
    for linha in linhas:
        linha = linha.strip()
        # Remove vírgula extra no fim, se houver
        if linha.endswith(','):
            linha = linha[:-1]
        # Separa os valores e remove possíveis espaços
        valores_str = [v.strip() for v in linha.split(',') if v.strip() != '']
        # Converte para float (ou int, se preferir)
        try:
            valores = [float(v) for v in valores_str]
        except ValueError:
            print("Erro na conversão dos valores. Certifique-se de que todos são numéricos.")
            exit()
        matriz.append(valores)
    
    # Converte zeros fora da diagonal para INF
    n = len(matriz)
    for i in range(n):
        # Confirma que a linha tem o número correto de colunas
        if len(matriz[i]) != n:
            print("Erro: a matriz não é quadrada!")
            exit()
        for j in range(n):
            if i != j and matriz[i][j] == 0:
                matriz[i][j] = INF
    return matriz