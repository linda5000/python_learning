# encoding:utf-8

import configparser
import os
from public.globalpath import config_path

class Config:
    def __init__(self):
        self.path = config_path


    def getConfig(self,section,key):
        config = configparser.ConfigParser()
        config.read(self.path + "config.ini",encoding='utf8')
        # return config[section][key]
        return config.get(section, key)

    def getTest(self,section,key):
        config = configparser.ConfigParser()
        config.read(self.path + "test.ini",encoding='utf8')
        # return config[section][key]
        return config.get(section, key)

def main():
    value = Config().getConfig("database", "user")
    print(value)

if __name__ == '__main__':
    main()