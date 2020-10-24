import logging


# Create a class and some configurations to load the files
class LogGenerator:

    @staticmethod
    def logGen():
        logging.basicConfig(filename='./Logs/automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # logger.warning('This should go in the file.')
        # print(logger.handlers)
        return logger

        # logging.getLogger().setLevel(logging.INFO)
        # logger = logging.getLogger("Logs")
        # logger.handlers = []

        # logging.basicConfig(level=logging.INFO,
        #                     format='%(asctime)s: [%(levelname)s] - %(message)s',
        #                     filename='./Logs/automation.log')
        # logger = logging.getLogger()
        # logger.warning('This should go in the file.')
        # print(logger.handlers)
