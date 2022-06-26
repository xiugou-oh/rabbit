
import pytest

from common.yml_util import clear_extract_yaml
from common.log_util import clear_log


@pytest.fixture(scope='session', autouse=True)
# 在每次会话前清除extract.yaml和log文件
def clear_yaml():
    clear_extract_yaml()
    clear_log()

