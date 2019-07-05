from libs.base_work import LoginClass
class Teacher(LoginClass):
    def apiTeacher(self):
        # 添加教师接口
        url = '/admin.php?m=mgr/member2.saveMemberInfo&id='
        # /admin.php?m=mgr/member2.saveMemberInfo&id=
        # 添加教师传参数据
        teacher_data = {
            'username': '13524270185',
            'realname': '123',
            'password': '123456',
            'sex': 1,
            'roleid': 8,
            'orid1': 107,
            'email': '13524260185@163.com',
            'phone': '13524270185',
            'location_p': '广东省',
            'location_c': '深圳市',
            'location_a': '宝安区',
            'address': '西乡',
            'introduce': '呵呵',
            'type': 1
        }
        # 登录
        self.apiLogin()
        # print('cookies is',self.cookies)
        #添加教师
        result1 = self.http_send(url=url,data=teacher_data,cookies=self.cookies)


        # # #查询添加教师是否成功
        # check_url = '/admin.php?m=mgr/member2.memberlist&type=1'
        # # /admin.php?m=mgr/member2.memberlist&type=1
        # result2 = self.http_send(method='get',url=check_url,cookies=self.cookies)
        return result1

if __name__ == '__main__':
    result = Teacher()
    print(result.apiTeacher())