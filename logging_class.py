import time
import logging
import logging.config
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s",datefmt="%m/%d/%Y %H:%M:%S")


class Logging:
    """can import logging to your application by simply import logging
       there are different block levels in logging with different configuration options,how to log different modules,how you use different log handelrs,how to capture stack traces in your log,how to use rotating file handlers (there are 5 different log levels)
       they are:
       1-debug2-info3-warning4-error5-critical"""
    def logging_method(self):
        #indicate severity of the events only warning error crtitical are printed
        logging.debug("this is debug message")
        logging.info("this is info message")
        logging.warning("this is warning message")
        logging.error("this is error message")
        logging.critical("this is critical message")
        logger = logging.getLogger(__name__)
        logger.debug("This is debugger bod")
        logger.propagate = False
    def logging_handler_method(self):
        logger = logging.getLogger(__name__)
        # Stream Handler
        stream_han = logging.StreamHandler()
        file_han=logging.FileHandler('./file.log')
        #file level and format
        stream_han.setLevel(logging.WARNING)
        file_han.setLevel(logging.ERROR)
        #Formatter
        formatter = logging.Formatter("%(name)s- %(levelname)s-%(message)s")
        stream_han.setFormatter(formatter)
        file_han.setFormatter(formatter)
        #logger add handler
        logger.addHandler(stream_han)
        logger.addHandler(file_han)
        #set logger message
        logger.warning('this is warning')
        logger.error('this is an error')
    def logging_conf_file(self):
        logging.config.fileConfig('./logging.conf','a')
        logger = logging.getLogger('simpleExample')
        logger.debug('this is a debug message') 
        logger.close()      
    def stack_traces(self):
        try:
            a=[1,2,3]
            val=a[4]
        except IndexError as e:
            logging.error(e,exc_info=True)
    def rotationg_file_handler(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # roll over after 2kb and keep backup logs app.log.1 to etc
        handler = RotatingFileHandler('./app.log',maxBytes=2000,backupCount=5)
        logger.addHandler(handler)
        
        for _ in range(100000):
            logger.info('hello_world') 
    def time_rotating_file_handler(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = TimedRotatingFileHandler('./timelogs.log',interval=5,backupCount=5,when='s')
        logger.addHandler(handler)
        for _ in range(6):
            logger.info('hello world')
            time.sleep(5)
            
        
        
        
                       