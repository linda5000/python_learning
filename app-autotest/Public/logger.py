import logging
import os
from Common.global_path import log_path

class Log:

    def __init__(self,logname):
        self.mylog = logging.getLogger(logname)
        self.mylog.setLevel(logging.INFO)
        self.logpath = log_path + "web_autoTest.log"

    def setFormatter(self):
        fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'
        formatter = logging.Formatter(fmt, datefmt)
        return formatter

    def add_StreamHandler(self,logLevel=None):
        handler = logging.StreamHandler()
        handler.setFormatter(self.setFormatter())
        if logLevel != None:
            handler.setLevel(logLevel)
        self.mylog.addHandler(handler)

    def add_RotatingFileHandler(self,logLevel=None,maxBytes=1024*1024*100,backupCount=10):
        from logging.handlers import RotatingFileHandler
        handler = RotatingFileHandler(self.logpath, maxBytes, backupCount)
        handler.setFormatter(self.setFormatter())
        if logLevel != None:
            handler.setLevel(logLevel)
        self.mylog.addHandler(handler)

    def info(self,message):
        self.mylog.info(message)

    def warn(self,message):
        self.mylog.warning(message)

    def debug(self,message):
        self.mylog.debug(message)

    def error(self,message):
       self.mylog.error(message)

    def critical(self,mesaage):
        self.mylog.critical(mesaage)

    def exception(self,message):
        self.mylog.exception(message)


myLog = Log("web_autoTest")
myLog.add_StreamHandler(logging.INFO)
myLog.add_RotatingFileHandler(logging.INFO)

