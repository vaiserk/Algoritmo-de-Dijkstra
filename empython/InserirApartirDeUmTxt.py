import math

def ler_grafo_de_arquivo(nome_arquivo):

    INF = math.inf
    matriz = []
    
    try:
        with open(nome_arquivo, 'r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado!")
        exit()
    for linha in linhas:
        linha = linha.strip()
        if linha.endswith(','):
            linha = linha[:-1]
        valores_str = [v.strip() for v in linha.split(',') if v.strip() != '']
        try:
            valores = [float(v) for v in valores_str]
        except ValueError:
            print("Erro na conversão dos valores. Certifique-se de que todos são numéricos.")
            exit()
        matriz.append(valores)
    
    n = len(matriz)
    for i in range(n):
        if len(matriz[i]) != n:
            print("Erro: a matriz não é quadrada!")
            exit()
        for j in range(n):
            if i != j and matriz[i][j] == 0:
                matriz[i][j] = INF
    return matriz