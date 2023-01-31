from timeit import timeit

def append_em_lista():

    nova_lista = []

    for el in range(1000):
        nova_lista.append(el ** 2 ** 6 / 3)

    return nova_lista


def list_comp():

    return [el ** 2 ** 6 / 3 for el in range(1000)]


"""

    Executando no escopo global
    Repetindo por 100 vezes

"""

print(
    'append',
    timeit("append_em_lista()", globals=globals(), number=10000)
)

print(
    'list_comp',
    timeit("list_comp()", globals=globals(), number=10000)
)