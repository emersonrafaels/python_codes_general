from Loguru_Add_Template_com_arquivo_ii import configure_logging

logger = configure_logging(APP_NAME="LOGURU_STUDY")

logger.debug("Logando DEBUG")
logger.info("Logando INFO")
logger.warning("Logando WARNING")
logger.error("Logando ERROR")
logger.critical("Logando CRITICAL")