"""
Exemplo 6.
Decorator
"""
import logging
from functools import wraps

# CRIANDO O FORMATO DO LOG
log_format = '%(asctime)s:%(filename)s:%(levelname)s:%(message)s'

# DEFININDO AS CONFIGURAÇÕES DO LOG
logging.basicConfig(filename='exemplo_6.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)


logger = logging.getLogger('root')

def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        l_msg = "func:{} args:{} kwargs:{} result:{}".format(func.__name__, args, kwargs, result)
        logger.debug(l_msg)
        return result
    return  inner

@log
def add(x, y):
    return x + y

add(5, 7)