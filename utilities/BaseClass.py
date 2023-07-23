import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]  # enables to print from the test which this method is called in output.
        logger = logging.getLogger(logger_name)  # created an object from logging class

        filehandler = logging.FileHandler(
            'orangehrm.log')  # passing the file location. Here a file is created with logfile.log name and all logs will be sent there.
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)  # Connecting formatting and file handling
        logger.addHandler(
            filehandler)  # There is a other class called file handler we have to pass file handler object to it
        
        # In above statement logger is asking information about in which file i have to print and what is the format
        # File handler is nothing but the file location
        # File location will come from parent loging not the object
        logger.setLevel(logging.DEBUG)
        return logger
        


