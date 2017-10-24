import logging
import time


class Log:
    def __init__(self,name,filename=None):
        self.name = name
        if filename is None:
            self.filename = 'log_' + time.strftime('%Y_%m_%d') + '.txt'
        else:
            self.filename = filename
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(self.name)

        self.sh = logging.StreamHandler()
        self.sh.setFormatter(self.formatter)
        self.logger.addHandler(self.sh)

        self.fh = logging.FileHandler(self.filename,encoding='utf-8')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        self.nameToLevel = {
            'CRITICAL': logging.CRITICAL,
            'FATAL': logging.FATAL,
            'ERROR': logging.ERROR,
            'WARN': logging.WARNING,
            'WARNING': logging.WARNING,
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG
        }
        self.setLevel("INFO")

    def setLevel(self,level):
        if level in self.nameToLevel:
            self.logger.setLevel(self.nameToLevel[level])

    def setshLevel(self,level):
        if level in self.nameToLevel:
            self.sh.setLevel(self.nameToLevel[level])

    def setfhLevel(self,level):
        if level in self.nameToLevel:
            self.fh.setLevel(self.nameToLevel[level])

    def debug(self,content):
        self.logger.debug(content)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def info(self,content):
        self.logger.info(content)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def warning(self, content):
        self.logger.warning(content)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def error(self, content):
        self.logger.error(content)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def critical(self,content):
        self.logger.critical(content)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)























