import os
import yaml


# 读取接口关联的yml(如token)
def read_extract_yaml(key):
    with open(os.getcwd() + '/extract.yaml', mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入接口关联的yml(如token)
def write_extract_yaml(data):
    with open(os.getcwd() + '/extract.yaml', mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清空接口关联的yml(如token)
def clear_extract_yaml():
    with open(os.getcwd() + '/extract.yaml', mode='w', encoding='utf-8') as f:
        f.truncate()


# 读取case_yaml文件
def read_caseInfo_yaml(yaml_name):
    with open(os.getcwd() + '/data/' + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 读取config.yaml文件
def read_config_yaml(yaml_name):
    with open(os.getcwd() + '/' + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value
