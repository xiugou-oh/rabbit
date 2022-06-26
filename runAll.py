import os
from time import sleep

import pytest
from common.log_util import logger

if __name__ == '__main__':
    sleep(1)
    logger.info(f'================================== 测试开始 ==================================')
    pytest.main()
    sleep(1)
    os.system("allure generate json -o reports --clean")
    logger.info(f'================================== 测试结束 ==================================')
