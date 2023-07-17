import functools

def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)


# Fibonacci with memoization
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]


# Automatic memoization
from functools import lru_cache


@functools.lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n - 1) + fib3(n -2)


# Iterative fibonacci
def fib4(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


# Generator fibonacci
from typing import Generator


def fib5(n: int) -> Generator[int, None, None]:
    yield 0 # Special case
    if n > 0: yield 1 # Special case
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    for i in fib5(50):
        print(i)
        breakpoint()
