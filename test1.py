import logging

logger = logging.getLogger()
logging.basicConfig(filename='test.log')

logger.debug("Debug test message")
logger.info("Info test message")
logger.warning("Warning test message")
logger.error("Error test message")
logger.critical("Critical test message")