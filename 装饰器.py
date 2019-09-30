def doca(func):
    def wrapper():
        print(func.__name__)
        func()

    return wrapper()
def fun():
    print('---1---')

print(doca(fun))