import configparser

# create object and store RawConfigParser class
# use read() and specify the location of the ini file
config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get("common info", 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'email')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getLogFilename():
        log_format = config.get('common info', 'log_file')
        return log_format