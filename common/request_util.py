import requests

session = requests.session()


def send_request(method, url, **kwargs):
    result = session.request(method=method, url=url, **kwargs)
    return result

    # 统一的发送请求方式
