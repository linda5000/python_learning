# encoding:utf-8

import configparser
import os


class ReadConfig:
    def __init__(self):
        self.path = "config.conf"


    def getConfig(self,section,key):
        config = configparser.ConfigParser()
        config.read(self.path,encoding='utf8')
        # return config[section][key]
        return config.get(section, key)


def main():
    value = ReadConfig().getConfig("server", "host")
    print(value)

if __name__ == '__main__':
    main()