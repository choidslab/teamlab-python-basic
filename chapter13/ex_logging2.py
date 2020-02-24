import logging

logger = logging.getLogger('myapp')  # logger
hdlr = logging.FileHandler('myapp.log')  # file handler

formatter = logging.Formatter("%(asctime)s %(levelname)s %(process)d %(message)s")  # log format 지정

hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.error('ERROR occured!')
logger.info('HERE WE ARE')
