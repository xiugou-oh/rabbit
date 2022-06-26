import logging
import os

logger = logging.getLogger("nanSheng")
logger.setLevel(logging.DEBUG)

# 输出格式
format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')

# 生成的log文件目录及名称
fl = logging.FileHandler(filename='logs/nanSheng.log', mode='a', encoding='utf-8')
fl.setFormatter(format)
sl = logging.StreamHandler()
sl.setFormatter(format)

logger.addHandler(fl)
logger.addHandler(sl)


# 清空log文件
def clear_log():
    with open(os.getcwd() + './logs/nanSheng.log', mode='w', encoding='utf-8') as f:
        f.truncate()
