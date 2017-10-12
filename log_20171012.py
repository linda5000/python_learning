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