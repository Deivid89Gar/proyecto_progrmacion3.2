class Nodo:
    """Representa un nodo y a sus vecinos (con el peso para llegar a cada uno)."""

    def __init__(self, nombre):
        self.nombre = nombre
        # Diccionario: vecino -> peso. Ejemplo: {"B": 4, "C": 2}
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso


class Grafo:
    """Guarda todos los nodos del grafo."""

    def __init__(self):
        # Diccionario: nombre -> objeto Nodo
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
        """Regresa (distancia_total, camino). Si no hay camino: (None, [])."""

        distancias = {}
        anteriores = {}
        visitados = set()

        # 1. Todos empiezan con distancia infinita y sin nodo anterior
        for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None

        # La distancia del inicio a sí mismo es 0
        distancias[inicio] = 0

        # 2. Mientras queden nodos por visitar
        while len(visitados) < len(self.nodos):
            # Buscar el nodo no visitado más cercano
            nodo_actual = None
            menor_distancia = float("inf")

            for nombre in self.nodos:
                if nombre not in visitados:
                    if distancias[nombre] < menor_distancia:
                        menor_distancia = distancias[nombre]
                        nodo_actual = nombre

            # Si ya no hay nodos alcanzables, terminamos
            if nodo_actual is None:
                break

            # Si llegamos al destino, terminamos
            if nodo_actual == destino:
                break

            visitados.add(nodo_actual)

            # 3. Revisar los vecinos del nodo actual
            nodo = self.nodos[nodo_actual]

            for vecino, peso in nodo.vecinos.items():
                nueva_distancia = distancias[nodo_actual] + peso

                # Si este camino es más corto, lo guardamos
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

        # Si el destino sigue en infinito, no hay camino
        if distancias[destino] == float("inf"):
            return None, []

        # 4. Construir el camino yendo del destino hacia atrás
        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()  # Lo damos vuelta para que vaya de inicio a destino
        return distancias[destino], camino


# ---------- Programa principal ----------
if __name__ == "__main__":
    # Creamos el grafo y agregamos las conexiones
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