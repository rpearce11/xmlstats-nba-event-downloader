import logging
import os

__author__ = 'Rich Pearce'


class LoggerUtil():

    def __init__(self):
        # create logger with 'spam_application'
        logger = logging.getLogger('NBA API logger')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        if not os.path.exists('../logs/'):
            os.makedirs('../logs/')
        fh = logging.FileHandler('../logs/nbaapilogger.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)

        logger.info('Starting NBA api logger')
