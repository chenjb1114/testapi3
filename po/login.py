import requests
from libs.Tools import BaseHttp
# 建立登录接口函数
def apiLogin():
    run =BaseHttp()
    # 登录接口
    login_url = '/admin.php?m=mgr/admin.chklogin&ajax=1'
    # 登录接口参数
    # 登录接口参数
    login_data = {
        'username': 'admin',
        'password': 'admin'
    }
    result = run.http_send(url=login_url,data=login_data)
    # data = result.headers
    # set_cookies = data['Set-Cookie']
    # php_data = set_cookies.split('=')
    # phpid = php_data[1]
    # return phpid
    return result.text


if __name__ == '__main__':
    a = apiLogin()
    print(a)


