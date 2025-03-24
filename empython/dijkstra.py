
import math

def dijkstra(graph, start, end):
    """
    graph: matriz de adjacência (list of lists), graph[u][v] = custo de u->v
    start: índice do vértice inicial (0 para vértice 1, 1 para vértice 2, etc.)
    end:   índice do vértice destino
    Retorna (distancia, caminho) onde:
      - distancia é a menor distância de start até end (ou math.inf se não houver)
      - caminho é uma lista de índices representando o trajeto
    """
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


def main():
    INF = math.inf

    # Matriz de adjacência de acordo com o diagrama (é um DIGRAFO)
    graph = [
        [0,   2,   INF, INF, INF,  INF],  
        [INF, 0,   INF, INF, INF,  INF],
        [1,   3,   0,   INF, INF,  INF],
        [2,   INF, 2,   0,   INF,  INF],
        [INF,   INF, 10, 5,   0,    4], 
        [5,   INF, INF, 1, INF,  0]   
    ]


    # Exemplo 2: caminho de 5 (índice 4) para 2 (índice 1)
    # Só para ver um caso que existe caminho

    comeco = input("digite o começo") 
    comeco = int(comeco) -1
    fim = input("digite o fim") 
    fim = int (fim) -1

    if ((comeco < 0 or comeco > 5) or (fim<0 or fim>5)):
        print("Imposivel!")
        exit()

    distancia, caminho = dijkstra(graph, comeco, fim)
    if distancia == INF:
        print(f"Não existe caminho de {comeco+1} para {fim+1}.")
    else:
        #path são os indices portanto se soma +1 para cada iten no vetor
        melhor_caminho = [x+1 for x in caminho]
        print(f"Distância de {comeco+1} para {fim+1} = {distancia}")
        print(f"Caminho: {melhor_caminho}")


if __name__ == "__main__":
    main()

