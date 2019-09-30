def fib_0(times):

    n = 0

    a,b = 0,1

    while n < times:

        print(b)

        # yield b

        a,b = b,a+b

        n += 1

    return 'done'

def fib_1(times):

    n,a,b = 0,0,1

    l = []

    while n < times:

        l.append(b)

        a,b = b, a+b

        n += 1

    return  l

class Fib(object):

    def __init__(self,max):

        self.max  = max
        self.a, self.n, self.b = 0,0,1

    def __iter__(self):

        return self

    def __next__(self):

        if self.n < self.max:

            r = self.b
            self.a,self.b = self.b,self.a+self.b
            self.n += 1
            return  r
        raise StopIteration()

def fib_2(times):

    n = 0

    a,b = 0,1

    while n < times:

        yield b

        a,b = b ,a+b

        n += 1
    return 'done'


print(fib_1(5))
# f = fib_2(5)
#
# for i in f:
#     print(i)



# p = Fib(5)
#
# for i in p:
#
#     print(i)


