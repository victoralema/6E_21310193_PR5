#Victor Eduardo Aleman Padilla 21310193

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  # Inicializa el diccionario de padres, donde cada vértice es su propio padre al inicio
        self.rank = {v: 0 for v in vertices}   # Inicializa el diccionario de rangos (usado para la optimización de Union-Find)

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression: hace que todos los vértices en el camino apunten directamente al padre
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:  # Union by rank: une el conjunto de menor rango al de mayor rango para mantener el árbol bajo
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_minimum_spanning_tree(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Ordena las aristas por peso
    uf = UnionFind(vertices)  # Inicializa la estructura Union-Find con los vértices
    minimum_spanning_tree = []
    for edge in edges:
        v1, v2, weight = edge
        if uf.find(v1) != uf.find(v2):  # Si los vértices v1 y v2 no están en el mismo conjunto
            uf.union(v1, v2)  # Une los conjuntos de v1 y v2
            minimum_spanning_tree.append(edge)  # Agrega la arista al árbol de expansión mínima
            # Si ya se han incluido suficientes aristas para conectar todos los vértices menos uno
            if len(minimum_spanning_tree) == len(vertices) - 1:
                break  # Termina el algoritmo

    return minimum_spanning_tree  # Retorna el árbol de expansión mínima encontrado

def kruskal_maximum_spanning_tree(vertices, edges):
    edges.sort(key=lambda x: x[2], reverse=True)  # Ordena las aristas por peso en orden descendente
    uf = UnionFind(vertices)  # Inicializa la estructura Union-Find con los vértices
    maximum_spanning_tree = []
    for edge in edges:
        v1, v2, weight = edge
        if uf.find(v1) != uf.find(v2):  # Si los vértices v1 y v2 no están en el mismo conjunto
            uf.union(v1, v2)  # Une los conjuntos de v1 y v2
            maximum_spanning_tree.append(edge)  # Agrega la arista al árbol de expansión máxima
            # Si ya se han incluido suficientes aristas para conectar todos los vértices menos uno
            if len(maximum_spanning_tree) == len(vertices) - 1:
                break  # Termina el algoritmo

    return maximum_spanning_tree  # Retorna el árbol de expansión máxima encontrado

# Definición del almacén
levels = range(1, 7)  # Niveles del almacén: del 1 al 6
columns = range(1, 6)  # Columnas del almacén: del 1 al 5
vertices = [(level, column) for level in levels for column in columns]  # Lista de todas las ubicaciones en el almacén

# Definición de las aristas (con pesos aleatorios para simulación)
import random
edges = []
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        v1 = vertices[i]  # Vértice 1
        v2 = vertices[j]  # Vértice 2
        weight = random.randint(1, 100)  # Peso aleatorio entre 1 y 100 (puedes ajustar este rango según sea necesario)
        edges.append((v1, v2, weight))  # Agrega la arista (v1, v2, weight) a la lista de aristas

# Ejecución de Kruskal para encontrar el árbol de expansión mínima
minimum_spanning_tree = kruskal_minimum_spanning_tree(vertices, edges)

# Ejecución de Kruskal para encontrar el árbol de expansión máxima
maximum_spanning_tree = kruskal_maximum_spanning_tree(vertices, edges)

# Función para encontrar el mínimo y máximo costo
def find_min_max_cost(queries, minimum_spanning_tree, maximum_spanning_tree):
    min_cost = float('inf')  # Inicializa el costo mínimo como infinito
    max_cost = float('-inf')  # Inicializa el costo máximo como menos infinito
    for query in queries:
        level, column = query  # Obtiene el nivel y columna de la consulta
        for edge in minimum_spanning_tree:
            (level1, column1), (level2, column2), cost = edge  # Obtiene los vértices y el costo de la arista
            if (level1 == level and column1 == column) or (level2 == level and column2 == column):  # Si la arista conecta con el nivel y columna de la consulta
                if cost < min_cost:
                    min_cost = cost  # Actualiza el costo mínimo si es menor
        for edge in maximum_spanning_tree:
            (level1, column1), (level2, column2), cost = edge  # Obtiene los vértices y el costo de la arista
            if (level1 == level and column1 == column) or (level2 == level and column2 == column):  # Si la arista conecta con el nivel y columna de la consulta
                if cost > max_cost:
                    max_cost = cost  # Actualiza el costo máximo si es mayor
    return min_cost, max_cost  # Retorna el costo mínimo y máximo encontrados

# Ejemplo de uso para encontrar mínimo y máximo coste para ubicaciones ingresadas por el usuario
queries = [(3, 4), (1, 2), (5, 5)]  # Ejemplos de ubicaciones (nivel, columna)
min_cost, max_cost = find_min_max_cost(queries, minimum_spanning_tree, maximum_spanning_tree)

# Imprime el árbol de expansión mínima encontrado
print("Árbol de expansión mínima:")
for edge in minimum_spanning_tree:
    print(edge)

# Imprime el árbol de expansión máxima encontrado
print("\nÁrbol de expansión máxima:")
for edge in maximum_spanning_tree:
    print(edge)

# Imprime el costo mínimo y máximo encontrados
print("\nMínimo costo encontrado:", min_cost)
print("Máximo costo encontrado:", max_cost)
