class Test(object):

    def __init__(self,func):

        print('初始化')
        print('func name is %s'%func.__name__)
        self.func = func

    def __call__(self, *args, **kwargs):
        print('---修饰器的功能---')
        self.func()

@Test

def test():
    print('---test---')

test()