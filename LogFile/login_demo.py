import logging
import time

nowtime = time.strftime("%Y%m%d%H%M%S")
# 使用logging提供的模块级别的函数记录日志

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 时间、等级、内容
# logging.basicConfig(filename='./Test1.log', level=logging.DEBUG, format=LOG_FORMAT)
#
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%M/%D %H:%M:%S %p"
logging.basicConfig(filename="./" + nowtime + '.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
