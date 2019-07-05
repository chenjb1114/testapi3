import unittest
from po.MemberCenter.addTeacher import Teacher
from libs.Tools import VerifyClass

class TestTeacherApi(VerifyClass):

    def setUp(self):
        self.p = Teacher()

    def test_teacher_success_001(self):
        result1 = self.p.apiTeacher()
        self.verify_html(result1,'保存成功')

if __name__ == '__main__':
    unittest.main()