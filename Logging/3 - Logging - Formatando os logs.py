"""
Exemplo 3.
Como personalizar o log
"""
import logging

# CRIANDO O FORMATO DO LOG
log_format = '%(asctime)s:%(filename)s:%(levelname)s:%(message)s'

# DEFININDO AS CONFIGURAÇÕES DO LOG
logging.basicConfig(filename='exemplo_3.log',
                    level=logging.DEBUG,
                    format=log_format)


logger = logging.getLogger('root')

logger.info('Olá Marilene')
logger.debug('Hoje a noite')
logger.critical('vinho, Tainha, e ...')