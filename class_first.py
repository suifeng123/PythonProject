class D:
    def bar(self):
        print 'D.bar'
class C(D):
    
    def bar(self):
        print 'C.bar'
class B(D):

    def bar(self):
        print 'D.bar'
class A(B,C):
    def bar(self):
        print 'A.bar'
a = A()
a.bar()
