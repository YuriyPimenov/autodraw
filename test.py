class A(object):
    def t(self):
        return 1

class B(object):
    def t(self):
        return 2

class C(B,A):
    def t(self):
        return super().t()

print(C())