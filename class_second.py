# -*- utf-8 -*-
#��ʽ�� ����˳����A-->B-->C--->D
class D(object):

    def bar(self):
        print 'D.bar'
class B(D):
    def bar(self):
        print 'B.bar'
class C(D):
    def bar(self):
        print 'C.bar'
class A(B,C):
    def bar(self):
        print 'A.bar'
a = A()
a.bar()

