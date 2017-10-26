import logging
logger = logging.getLogger("python全栈1期")
logger.setLevel(logging.INFO)

sh =logging.StreamHandler()
sh.setLevel(logging.INFO)

fh=logging.FileHandler("test.log",encoding='utf-8')
fh.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)

logger.addHandler(sh)
logger.addHandler(fh)

logger.info("这个是我们的第一条日志")
logger.debug("这个是我们的第二条日志")
logger.warning("这个是我们的第三条日志")

logging.info("这个是我们的第1条日志")
logging.debug("这个是我们的第2条日志")
logging.warning("这个是我们的第3条日志")





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