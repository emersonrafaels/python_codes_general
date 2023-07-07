import sys
from pathlib import Path

from loguru import logger

logger.remove()

logger.add(sys.stderr,
           colorize=True,
           format="{time} - {level} - {message}",
           level="INFO")

logger.add("file_loguru_log_{}".format(Path(__file__).stem.replace(" ", "_")),
            colorize=True,
            format="{time} - {level} - {message}",
            level="INFO")

logger.debug("Logando DEBUG")
logger.info("Logando INFO")
logger.warning("Logando WARNING")
logger.error("Logando ERROR")
logger.critical("Logando CRITICAL")