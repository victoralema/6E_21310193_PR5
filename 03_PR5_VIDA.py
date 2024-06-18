#Victor Eduardo Aleman Padilla 21310193
import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict

class KruskalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Árbol de Máximo y Mínimo Coste (Kruskal)")
        
        # Definición del grafo como un diccionario de listas de tuplas con pesos entre nodos
        self.graph = {
            'Trabajo': [('Casa', 1), ('Ceti', 4)],
            'Casa': [('Trabajo', 1), ('Ceti', 2), ('Servicio', 5)],
            'Ceti': [('Trabajo', 4), ('Casa', 2), ('Servicio', 1)],
            'Servicio': [('Casa', 5), ('Ceti', 1)]
        }
        
        # Creación de la etiqueta para el resultado
        self.label_output = ttk.Label(master, text="Resultado:")
        self.label_output.grid(row=0, column=0, padx=10, pady=10)
        
        # Creación del cuadro de texto para mostrar el resultado
        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.grid(row=1, column=0, padx=10, pady=10)
        
        # Botón para calcular el Árbol de Máximo y Mínimo Coste usando Kruskal
        self.run_button_kruskal = ttk.Button(master, text="Calcular Árbol de Máximo y Mínimo Coste", command=self.calculate_min_max_spanning_tree)
        self.run_button_kruskal.grid(row=2, column=0, padx=10, pady=10)

    def calculate_min_max_spanning_tree(self):
        # Mostrar un mensaje informativo
        messagebox.showinfo("Información", "Se seleccionó el algoritmo de Kruskal.")
        
        # Obtener todas las aristas del grafo
        edges = self.get_edges()
        # Calcular el Árbol de Mínimo Coste
        mst_min = self.kruskal(edges, min=True)
        # Calcular el Árbol de Máximo Coste
        mst_max = self.kruskal(edges, min=False)
        
        # Borrar el contenido anterior del cuadro de texto de resultado
        self.output_text.delete(1.0, tk.END)
        
        # Mostrar el Árbol de Mínimo Coste
        self.output_text.insert(tk.END, "Árbol de Mínimo Coste:\n")
        self.output_text.insert(tk.END, f"Coste total: {sum(edge[2] for edge in mst_min)}\n")
        for edge in mst_min:
            self.output_text.insert(tk.END, f"{edge[0]} - {edge[1]} : {edge[2]}\n")
        
        # Mostrar el Árbol de Máximo Coste
        self.output_text.insert(tk.END, "\nÁrbol de Máximo Coste:\n")
        self.output_text.insert(tk.END, f"Coste total: {sum(edge[2] for edge in mst_max)}\n")
        for edge in mst_max:
            self.output_text.insert(tk.END, f"{edge[0]} - {edge[1]} : {edge[2]}\n")

    def get_edges(self):
        edges = []
        # Recorrer el grafo y obtener todas las aristas
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                edges.append((node, neighbor, weight))
        return edges
    
    def find(self, parent, node):
        # Función para encontrar el representante del conjunto de un nodo
        if parent[node] == node:
            return node
        else:
            return self.find(parent, parent[node])

    def union(self, parent, rank, node1, node2):
        # Función para unir dos conjuntos disjuntos
        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    def kruskal(self, edges, min=True):
        # Implementación del algoritmo de Kruskal para encontrar el MST
        edges.sort(key=lambda x: x[2], reverse=not min)  # Ordenar las aristas por peso
        parent = {}  # Diccionario para almacenar el padre de cada nodo
        rank = {}  # Diccionario para almacenar la altura del árbol

        # Inicializar cada nodo como su propio padre y con altura 0
        for node in self.graph:
            parent[node] = node
            rank[node] = 0

        mst = []  # Lista para almacenar las aristas del MST

        # Recorrer todas las aristas en orden de peso
        for edge in edges:
            node1, node2, weight = edge
            # Comprobar si los nodos de la arista pertenecen a diferentes conjuntos
            if self.find(parent, node1) != self.find(parent, node2):
                self.union(parent, rank, node1, node2)  # Unir los conjuntos
                mst.append(edge)  # Agregar la arista al MST

        return mst  # Devolver el MST

def main():
    root = tk.Tk()  # Crear la ventana principal
    kruskal_gui = KruskalGUI(root)  # Crear una instancia de la interfaz gráfica
    root.mainloop()  # Iniciar el bucle principal de eventos

if __name__ == "__main__":
    main()  # Ejecutar la función main si este script es el programa principal
