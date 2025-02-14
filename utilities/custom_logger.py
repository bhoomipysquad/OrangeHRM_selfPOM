# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#
#        logging.basicConfig(filename = ".\\Logs\\automation.log",
#                         format = '%(asctime)s: %(levelname)s: %(message)s' ,
#                         datefmt = '%m/%d/%Y %I:%M:%S %p' )
#
#        #make object of logging
#        logger = logging.getLogger()
#        logger.setLevel(logging.INFO)
#        return logger
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Set up the log directory
        log_dir = "./Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure logging to log to a file and console
        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            level=logging.info(),  # Capture logs of level DEBUG and above
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )

        # Create a logger object
        logger = logging.getLogger()

        # Add a console handler to print logs to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Print logs to console with DEBUG level
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger
