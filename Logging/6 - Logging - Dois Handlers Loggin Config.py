import logging
import logging.config

# OBTENDO O ARQUIVO DE CONFIGURAÇÕES
logging.config.fileConfig("dois_handlers_loggin.ini")

logger = logging.getLogger('root')

logger.info("Bananas2")