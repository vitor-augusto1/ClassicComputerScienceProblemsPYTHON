from typing import Optional, TypeVar, Generic, List
from edge import Edge
import sys
sys.path.insert(0, '../..')
from search_problems.generic_search import bfs, Node, node_to_path

V = TypeVar('V')  # Tipo dos vértices no grafo


# O papel de Graph é associar vértices e arestas
class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  # Retorna o número de vértices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))  # Retorna o número de arestas

    # Adiciona um vértice ao grafo e retorna o seu número
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])  # Adiciona uma lista vazia para conter as arestas
        return self.vertex_count - 1  # Devolve o índice do vértice adicionado

    # Esse é um grafo não direcionado, portanto, sempre adicionamos arestas nas
    # duas direções
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Adiciona uma aresta usando índices dos vértices (método auxiliar)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # Adiciona uma aresta consultando os indices dos vértices (método auxiliar)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Encontra o vértice em um índice especifico
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Encontra o indice de um vertice no grafo
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Encontra os vértices aos quais um vértice com determinado índice está conectado
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Consulta o índice de um vértice e encontra seus vizinhos (método auxiliar)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # Devolve todas as arestas associadas a um vértice em um índice
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Consulta o índice de um vértice e devolve suas arestas (método auxiliar)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Facilita a exibição elegante de um Graph
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles",
                                    "Riverside", "Phoenix", "Chicago", "Boston",
                                    "New York", "Atlanta", "Miami", "Dallas",
                                    "Houston", "Detroit", "Philadelphia",
                                    "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    ...
    print(city_graph)
    bfs_result: Optional[Node[V]] = bfs("Chicago",
                                        lambda x: x == "San Francisco",
                                        city_graph.neighbors_for_vertex)
    print(f"Neighbors for vertex: {city_graph.neighbors_for_vertex}")
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("Path from Chicago to San Francisco: ")
        print(path)
