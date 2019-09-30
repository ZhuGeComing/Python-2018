class Person(object):

    __num = 100

    num = 1000

    def __init__(self,name,age):

        self.name = name

        self.__num = age

    def showinfo(self):

        print(self.name)

        # print(self.age)

        print(self.__num)

    @classmethod

    def printNum(cls,num):

        cls.__num = num

        print(cls.__num)

    @classmethod

    def print__Num(cls):


        print(cls.__num)

    @staticmethod

    def add(a,b):

        return a+b


p = Person('zhangsan',12)

p.print__Num()

p.showinfo()

p.printNum(33)



