from datetime import datetime
from time import sleep
from functools import wraps

from medidor_de_tempo import medidor_de_tempo


@medidor_de_tempo
def delay(secs):

    """

        A FUNÇÃO REALIZA O SLEEP DE X SECS.

    """

    sleep(secs)

    return secs


print(delay(5))