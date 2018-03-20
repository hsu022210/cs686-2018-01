from logger import logger

class file_logger(logger):


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
    def log(self, log_level, message, output_file_name=None):
        if  self.__log_level__ >= log_level:
            if not output_file_name:
                output_file_name = "file_log.txt"
            my_file = open(output_file_name, "a")
            my_file.write(str(log_level) + ":" + message + "\n")
            my_file.close()
