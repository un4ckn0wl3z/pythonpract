import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)
logging = logging.getLogger(__name__)
# logging = logging.getLogger('book')
# logging = logging.getLogger('book.database')


logging.debug('TEST DEBUG')
logging.info('TEST INFO')
logging.warning('TEST WARNING')
logging.error('TEST ERROR')
logging.critical('TEST CRITICAL')
