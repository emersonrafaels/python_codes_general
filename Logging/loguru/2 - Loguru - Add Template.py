import sys

from loguru import logger

logger.remove()

logger.add(sys.stderr,
           format="{time} - {level} - {message}",
           level="INFO")

logger.debug("Logando DEBUG")
logger.info("Logando INFO")
logger.warning("Logando WARNING")
logger.error("Logando ERROR")
logger.critical("Logando CRITICAL")