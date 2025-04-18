
import math
from InserirApartirDeUmTxt import ler_grafo_de_arquivo

def dijkstra(graph, start, end):
    
    INF = math.inf
    n = len(graph)
    print(n)

    dist = [INF] * n
    dist[start] = 0
    visited = [False] * n
    
    predecessor = [-1] * n

    for _ in range(n):
        u = -1
        menor = INF
        for i in range(n):
            if not visited[i] and dist[i] < menor:
                menor = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True

        for v in range(n):
            if graph[u][v] != INF and not visited[v]:
                nova_dist = dist[u] + graph[u][v]
                if nova_dist < dist[v]:
                    dist[v] = nova_dist
                    predecessor[v] = u

    caminho = []
    if dist[end] != INF:
        atual = end
        while atual != -1:
            caminho.append(atual)
            atual = predecessor[atual]
        caminho.reverse()

    return dist[end], caminho

def mat():
    matriz = input("digite a b c d ou e para escoler a matriz: ")
    return matriz

def main():
    INF = math.inf
    

    try:
        matriz = mat()
        while matriz not in ("a", "b", "c", "d","e"):
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
        melhor_caminho = [x+1 for x in caminho]
        print(f"Distância de {comeco+1} para {fim+1} = {distancia}")
        print(f"Caminho: {melhor_caminho}")


if __name__ == "__main__":
    main()

