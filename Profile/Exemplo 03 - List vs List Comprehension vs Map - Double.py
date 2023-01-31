from timeit import timeit

import numpy as np

def double_number(x):

    return x*x


list_random = np.arange(1, 10000)


def list_double():

    nova_lista = []

    for value in list_random:
        nova_lista.append(double_number(value))

    return nova_lista


def comprehension_double():

    return [double_number(value) for value in list_random]


def map_double():

    return list(map(double_number, list_random))

"""

    Executando no escopo global
    Repetindo por 100 vezes

"""

print(
    'map',
    timeit("map_double()", globals=globals(), number=10000)
)

print(
    'list',
    timeit("list_double()", globals=globals(), number=10000)
)

print(
    'list_comp',
    timeit("comprehension_double()", globals=globals(), number=10000)
)