# encoding:utf-8

import configparser
import os
from Common.global_path import conf_path


class ReadConfig:
    def __init__(self,filename):
        self.path = conf_path + filename


    def getConfig(self,section,key):
        config = configparser.ConfigParser()
        config.read(self.path,encoding='utf8')
        return config.get(section, key)


