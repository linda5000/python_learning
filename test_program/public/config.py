# encoding:utf-8

import configparser
import os

class Config:
    def __init__(self,path=None):
        if path is None:
            self.path = '../conf/config.ini'
            print(path)
            # os.path.split(os.path.realpath(__file__))[0] 得到的是当前模块的目录
        else:
            self.path = path


    def getConfig(self,section,key):
        config = configparser.ConfigParser()
        config.read(self.path,encoding='utf8')
        # return config[section][key]
        return config.get(section, key)



def main():
    value = Config().getConfig("database", "user")
    print(value)

if __name__ == '__main__':
    main()