import logging

# OBTENDO O OBJETO LOGGER (QUE CONTÉM LEVEL, HANDLER, FORMATTER E FILTER)
logger = logging.getLogger('simple_example')

# DEFININDO O LEVEL DO LOGGER
logger.setLevel(logging.DEBUG)

# DEFININDO UM FORMATADOR
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# DEFININDO UM CONSOLE HANDLER (DEFINIREMOS UM LEVEL E UM FORMATTER)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# DEFININDO UM FILE HANDLER (DEFINIREMOS UM LEVEL E UM FORMATTER)
fh = logging.FileHandler("log.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# LOGGER, ADICIONANDO OS SEUS HANDLERS
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')