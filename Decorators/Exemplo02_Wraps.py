from datetime import datetime
from time import sleep
from functools import wraps


def medidor_de_tempo(func):

    @wraps(func)
    def aninhada(*args, **kwargs):
        tempo_inicial = datetime.now()

        resultado = func(*args, **kwargs)

        tempo_final = datetime.now()
        tempo = tempo_final - tempo_inicial
        print(f'{func.__name__} demorou {tempo.total_seconds()} segundos.')

        return resultado

    return aninhada


@medidor_de_tempo
def delay(secs):
    """Bota o código para dormir por `secs`."""
    sleep(secs)
    return secs


print(delay(5))