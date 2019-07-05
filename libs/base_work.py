from libs.Tools import BaseHttp
# 登录接口类
class LoginClass(BaseHttp):
    cookies = {
        'PHPSESSID': ''
    }
    def apiLogin(self):
        # 登录接口
        login_url = '/admin.php?m=mgr/admin.chklogin&ajax=1'
        # 登录接口参数
        login_data = {
            'username': 'admin',
            'password': 'admin'
        }
        result = self.http_send(url=login_url,data=login_data)
        # phpid = result.cookies['PHPSESSID']

        data = result.headers
        # print('data is',data)
        set_cookies = data['Set-Cookie']
        php_data = set_cookies.split('=')
        phpid = php_data[3].split(';')[0]
        # print('phpid is',phpid)
        self.cookies['PHPSESSID']=phpid
        # return result.text
        return phpid
