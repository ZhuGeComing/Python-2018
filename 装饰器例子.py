def makeBold(fn):
    def wrapped():
        return  '<b>'+fn()+'<b>'
    return wrapped

@makeBold

def test():
    return  'hello world'

print(test())