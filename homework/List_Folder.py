__author__ = "小黑"

import os


def list_folder(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.isfile(os.path.join(path, i)):
            print(os.path.join(path, i))
        else:
            list_folder(os.path.join(path, i))


path = "F:\软件"
list_folder(path)



