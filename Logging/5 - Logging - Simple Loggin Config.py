import logging
import logging.config

# OBTENDO O ARQUIVO DE CONFIGURAÇÕES
logging.config.fileConfig("simple_loggin.ini")

logger = logging.getLogger('root')

logger.info("Bananas")