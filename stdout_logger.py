from logger import logger

class stdout_logger(logger):


    """
    Constructor
    """
    def __init__(self, log_level):
        logger.__init__(self, log_level)


    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """
    def log(self, log_level, message):
        if self.__log_level__ >= log_level:
            print(str(log_level) + ":" + message)
