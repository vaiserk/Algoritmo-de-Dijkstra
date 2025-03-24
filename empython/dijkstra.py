
import math
from InserirApartirDeUmTxt import ler_grafo_de_arquivo

def dijkstra(graph, start, end):
    
    INF = math.inf
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    visited = [False] * n
    predecessor = [-1] * n

    for _ in range(n):
        # Acha o vértice u não-visitado com menor dist[u]
        u = -1
        menor = INF
        for i in range(n):
            if not visited[i] and dist[i] < menor:
                menor = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True

        # Relaxa as arestas que saem de u
        for v in range(n):
            if graph[u][v] != INF and not visited[v]:
                nova_dist = dist[u] + graph[u][v]
                if nova_dist < dist[v]:
                    dist[v] = nova_dist
                    predecessor[v] = u

    # Reconstruindo o caminho
    caminho = []
    if dist[end] != INF:
        atual = end
        while atual != -1:
            caminho.append(atual)
            atual = predecessor[atual]
        caminho.reverse()

    return dist[end], caminho

def mat():
    matriz = input("digite a b c ou d para escoler a matriz: ")
    return matriz

def main():
    INF = math.inf
    

    #importando matriz
    try:
        matriz = mat()
        while matriz not in ("a§b§c§d"):
            matriz = mat()
    except:
        print("erro!")
        

    graph_test = ler_grafo_de_arquivo(rf"C:\Users\ootav\OneDrive\Desktop\algo digistra\empython\adjacencia_{matriz}.txt")

    comeco = int(input("digite o começo: ") ) - 1;  
    fim = int(input("digite o fim: ") ) -1; 
    
    
    if ((comeco < 0 or comeco > len(graph_test)) or (fim<0 or fim>len(graph_test))):
        print("Imposivel!")
        exit()

    distancia, caminho = dijkstra(graph_test, comeco, fim)
    if distancia == INF:
        print(f"Não existe caminho de {comeco+1} para {fim+1}.")
    else:
        #path são os indices portanto se soma +1 para cada iten no vetor5
        melhor_caminho = [x+1 for x in caminho]
        print(f"Distância de {comeco+1} para {fim+1} = {distancia}")
        print(f"Caminho: {melhor_caminho}")


if __name__ == "__main__":
    main()

