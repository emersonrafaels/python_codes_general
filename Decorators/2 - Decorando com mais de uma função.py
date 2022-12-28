from functools import cache
from time import sleep

from medidor_de_tempo import medidor_de_tempo


@cache
@medidor_de_tempo
def delay(secs):

    """

        A FUNÇÃO REALIZA O SLEEP DE X SECS.

        PODEMOS DECORAR COM MAIS DE UMA FUNÇÃO
        NESSE CASO, ALÉM DE MEDIR O TEMPO, TEMOS A FUNÇÃO DE CACHÊ

    """

    sleep(secs)

    return secs


if __name__ == '__main__':

    print(delay(5), delay(5), delay(5))

