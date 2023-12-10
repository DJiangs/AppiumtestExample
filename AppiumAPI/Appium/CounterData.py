import datetime
import unittest
import os


class Counter(unittest.TestCase):

    def setUp(self):
        self.a = 5
        self.b = 3
        self.c = 0

    def test_add(self):
        self.c = self.a + self.b
        self.assertEqual(self.c, 8)

    def test_sub(self):
        self.c = self.a - self.b
        self.assertEqual(self.c, 2)

    @unittest.skip("跳过测试用例test_mulyiply")
    def test_multiply(self):
        self.c = self.a * self.b
        self.assertEqual(self.c, 15)

    def test_integer(self):
        self.c = self.a % self.b
        self.assertEqual(self.c, 1)

    def tearDown(self):
        pass


# 利用unittest中的TestSuite模块构造测试集
suite = unittest.TestSuite()
suite.addTest(Counter("test_add"))
suite.addTest(Counter("test_sub"))
suite.addTest(Counter("test_multiply"))
suite.addTest(Counter("test_integer"))

BasePath = os.path.dirname(__file__)  # 获取当前文件所在路径

if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   # report_path = os.path.join(os.getcwd(), f"test_report_{now}.html")
    fp =BasePath + "\\report"
    # filename为文件名称，report_dir报告输出位置，title测试标题，tester测试测试人员，desc描述
    runner = unittest.TestRunner(suite, filename=f"test_report_{now}.html", report_dir=fp, title="测试报告", tester="LLEI", desc="LLEI执行的测试用例")
    runner.run()

