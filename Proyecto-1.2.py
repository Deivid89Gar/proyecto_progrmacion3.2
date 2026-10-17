class Nodo:
    """Representa un nodo y a sus vecinos (con el peso para llegar a cada uno)."""

    def __init__(self, nombre):
        self.nombre = nombre
        
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso


class Grafo:
    """Guarda todos los nodos del grafo."""

    def __init__(self):
        
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def agregar_arista(self, origen, destino, peso):
        # Si los nodos no existen, se crean
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        # Se puede ir en ambos sentidos con el mismo peso
        self.nodos[origen].agregar_vecino(destino, peso)
        self.nodos[destino].agregar_vecino(origen, peso)

    def dijkstra(self, inicio, destino):
        

        distancias = {}
        anteriores = {}
        visitados = set()

        
        for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None

       
        distancias[inicio] = 0

        
        while len(visitados) < len(self.nodos):
            
            nodo_actual = None
            menor_distancia = float("inf")

            for nombre in self.nodos:
                if nombre not in visitados:
                    if distancias[nombre] < menor_distancia:
                        menor_distancia = distancias[nombre]
                        nodo_actual = nombre

            
            if nodo_actual is None:
                break

            
            if nodo_actual == destino:
                break

            visitados.add(nodo_actual)

            
            nodo = self.nodos[nodo_actual]

            for vecino, peso in nodo.vecinos.items():
                nueva_distancia = distancias[nodo_actual] + peso

                
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

        
        if distancias[destino] == float("inf"):
            return None, []

        
        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()  # Lo damos vuelta para que vaya de inicio a destino
        return distancias[destino], camino


if __name__ == "__main__":
    
    grafo = Grafo()
    grafo.agregar_arista("A", "B", 4)
    grafo.agregar_arista("A", "C", 2)
    grafo.agregar_arista("B", "C", 1)
    grafo.agregar_arista("B", "D", 5)
    grafo.agregar_arista("C", "D", 8)
    grafo.agregar_arista("C", "E", 10)
    grafo.agregar_arista("D", "E", 2)
    grafo.agregar_arista("D", "F", 6)
    grafo.agregar_arista("E", "F", 3)

    print("Nodos disponibles:", ", ".join(grafo.nodos))

    while True:
        inicio = input("Nodo origen (o escribe 'salir'): ").strip().upper()
        if inicio == "SALIR":
            break
        destino = input("Nodo destino: ").strip().upper()

        if inicio not in grafo.nodos or destino not in grafo.nodos:
            print("Error: uno de los nodos no existe.")
        else:
            distancia, camino = grafo.dijkstra(inicio, destino)
            if distancia is None:
                print("No existe un camino entre esos nodos.")
            else:
                print("Ruta más corta:", " -> ".join(camino))
                print("Costo total:", distancia)
        print()