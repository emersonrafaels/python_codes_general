from time import sleep
from medidor_de_tempo import medidor_de_tempo


@medidor_de_tempo
def delay(secs):

    """

        A FUNÇÃO REALIZA O SLEEP DE X SECS.

    """

    sleep(secs)

    return secs


if __name__ == '__main__':

    delay(3)