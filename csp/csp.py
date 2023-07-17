from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod


V = TypeVar('V') # Type for the variable
D = TypeVar('D') # Type for the domain


# Base class for all restrictions
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                error_msg = "Every variable shoud have a domain assigned to it"
                raise LookupError(error_msg)

    def add_contraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                error_msg = "Variable in constraint not in CSP"
                raise LookupError(error_msg)
            else:
                self.constraints[variable].append(constraint)


    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True


    def backtracking_search(
            self, assignment: Dict[V, D] = {}
    ) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables):
            return assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None
