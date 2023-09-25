from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')  # Tipo dos vértices no grafo


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  # Retorna o número de vértices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))  # Retorn ao número de arestas

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
