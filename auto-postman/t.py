# -*- coding: utf-8 -*-
import unittest

import case_template

from HTMLTestRunner import HTMLTestRunner

records = {
    '1': [
        ('danmu', 'POST', 'http://api.live.bilibili.com/msg/send', {}, {}, {}),
        ('gift', 'GET', 'http://api.live.bilibili.com/gift', {}, {}, {}),
    ],

    '2': [
        ('danmu', 'POST', 'http://api.live.bilibili.com/msg/send', {}, {}, {}),
        ('gift', 'GET', 'http://api.live.bilibili.com/gift', {}, {}, {}),
    ],
}


def gen_test_suite():
    global records

    testsuit = unittest.TestSuite()
    for scence, cases in records.iteritems():
        scence_cls = type('BiliTest_%s' % scence, (unittest.TestCase,), {
            '__doc__': u'这是场景%s' % scence,
        })

        # 动态生成测试方法
        cases_name = []
        for case in cases:
            fn_name = 'test_' + case[0]
            fn = getattr(case_template, '_'+case[1])
            fn.__doc__ = u'测试'
            setattr(scence_cls, fn_name, fn)
            cases_name.append(fn_name)

        # 添加测试用例到测试套件中
        for case_name in cases_name:
            t = scence_cls(case_name)
            testsuit.addTest(t)

    return testsuit


if __name__ == '__main__':
    # 生成测试报告
    with open('report.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='',
                                description='')
        runner.run(gen_test_suite())
