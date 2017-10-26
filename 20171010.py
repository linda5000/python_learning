import os
import logging

def f1(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.isdir(os.path.join(path, i)):
            f1(os.path.join(path, i))
        else:
            print(i)

def f2(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.isfile(os.path.join(path, i)):
            print(i)
        else:
            f2(os.path.join(path, i))


path = 'E:\学习资料'
# f1(path)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

