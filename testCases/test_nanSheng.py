import re

import pytest
from common.log_util import logger
from common.request_util import send_request
from common.yml_util import read_caseInfo_yaml, write_extract_yaml, read_extract_yaml, read_config_yaml


class Test_nanSheng:

    # 用户登录
    @pytest.mark.parametrize('caseInfo', read_caseInfo_yaml('test_userLogin.yml'))
    @pytest.mark.parametrize('config', read_config_yaml('config.yaml'))
    def test_userLogin(self, caseInfo, config):
        name = caseInfo['name']
        print(config['base']['base_url'])
        print(caseInfo['url'])
        url = config['base']['base_url'] + caseInfo['url']
        method = caseInfo['method']
        data = caseInfo['data']
        validate = caseInfo['validate']
        result = send_request(method, url, data=data)
        logger.info(f'{name}:{result.text}')
        assert validate['code'] == result.json()['code'] and validate['msg'] == result.json()['msg']

    # 获取用户id
    @pytest.mark.parametrize('config', read_config_yaml('config.yaml'))
    def test_getUserId(self, config):
        url = config['base']['base_url']
        method = "get"
        result = send_request(method, url)
        userId = re.search('input id="session_userid" type="hidden" value="(.*?)"', result.text)[1]
        write_extract_yaml({'userId': userId})
        userid = read_extract_yaml('userId')
        logger.info(f'获取到用户id：{userid}')

    # 用户访问个人中心
    @pytest.mark.parametrize('config', read_config_yaml('config.yaml'))
    def test_userCenter(self, config):
        userId = read_extract_yaml('userId')
        method = "post"
        url = config['base']['base_url'] + "/myself.jsp?userid=" + userId
        result = send_request(method, url)
        logger.info(f'访问个人中心状态码：{result.status_code}')

    # 获取帖子id
    @pytest.mark.parametrize('config', read_config_yaml('config.yaml'))
    def test_getArticleId(self, config):
        url = config['base']['base_url']+"/api/rest/nanshengbbs/v3.0/article/getArticle"
        method = 'get'
        result = send_request(method, url)
        articleId = re.search('"fid":"(.*?)"', result.text)[1]
        write_extract_yaml({'articleId': articleId})
        logger.info(f'获取到帖子id：{read_extract_yaml("articleId")}')
