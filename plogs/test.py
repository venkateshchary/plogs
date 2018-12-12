from plogs import get_logger

logging = get_logger()
logging.config(to_file=True)

logging.info('test')
