#Victor Eduardo Aleman Padilla 21310193
class Grafo:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices en el grafo
        self.grafo = []    # Lista para almacenar las aristas del grafo

    def agregar_arista(self, u, v, peso):
        """
        Función para agregar una arista al grafo.
        """
        self.grafo.append([u, v, peso])  # Agregar la arista como una lista [u, v, peso]

    def encontrar(self, padre, i):
        """
        Función para encontrar el conjunto al que pertenece el nodo 'i'.

        """
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])  # Aplicación de la compresión de camino

    def unir(self, padre, rango, x, y):
        """
        Función para unir dos conjuntos en uno solo.

        Args:
        padre: Lista de padres de los nodos.
        rango: Lista de rangos de los nodos para optimizar la unión.
        x, y: Nodos a unir.
        """
        raiz_x = self.encontrar(padre, x)  # Encontrar la raíz del nodo x
        raiz_y = self.encontrar(padre, y)  # Encontrar la raíz del nodo y

        # Unir los conjuntos según el rango
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal_mst(self, mst_type='max'):
        """
        Función para encontrar el Árbol de Máximo Coste o Mínimo Coste usando el algoritmo de Kruskal.
        """
        resultado = []  # Lista para almacenar el MST resultante
        i, e = 0, 0  # Contadores para recorrer las aristas y el MST resultante

        # Ordenar el grafo por peso en orden descendente si mst_type es 'max'
        self.grafo = sorted(self.grafo, key=lambda item: item[2], reverse=(mst_type=='max'))

        padre = []  # Lista para almacenar los padres de los nodos
        rango = []  # Lista para almacenar el rango de los nodos (para la optimización de unión)

        # Inicialización de los padres y rangos
        for nodo in range(self.V):
            padre.append(nodo)  # Cada nodo es su propio padre inicialmente
            rango.append(0)     # Inicialmente, el rango de cada nodo es 0

        # Mientras no se hayan agregado V-1 aristas al MST
        while e < self.V - 1:
            u, v, peso = self.grafo[i]  # Obtener la arista siguiente del grafo ordenado
            i = i + 1  # Incrementar el índice para la próxima arista

            x = self.encontrar(padre, u)  # Encontrar el conjunto de u
            y = self.encontrar(padre, v)  # Encontrar el conjunto de v

            # Si u y v están en conjuntos diferentes
            if x != y:
                e = e + 1  # Incrementar el contador de aristas agregadas al MST
                resultado.append([u, v, peso])  # Agregar la arista al MST
                self.unir(padre, rango, x, y)  # Unir los conjuntos de u y v

        return resultado  # Devolver el MST resultante

# Ejemplo de uso:
g = Grafo(6)  # Supongamos que tenemos 6 estaciones

# Agregamos las rutas con sus pesos (en este caso, tiempos de viaje)
g.agregar_arista(0, 1, 7)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 2, 8)
g.agregar_arista(1, 3, 9)
g.agregar_arista(1, 4, 7)
g.agregar_arista(2, 4, 5)
g.agregar_arista(3, 4, 15)
g.agregar_arista(3, 5, 6)
g.agregar_arista(4, 5, 8)

resultado = g.kruskal_mst(mst_type='max')  # Encontrar el Árbol de Máximo Coste
print("Rutas de transporte público óptimas (Máximo Coste):")
for u, v, peso in resultado:
    print(f"De la estación {u} a la estación {v}, tiempo de viaje: {peso} minutos")
