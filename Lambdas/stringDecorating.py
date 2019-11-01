def decorfun(name):
    def inner(n):
        result = name(n)
        result += "How are you?"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name

print(hello("John, "))


def decorfun(zhz):
    def inner(bongo):
        result = zhz(bongo)
        result += "How are you?"
        return result
    return inner

@decorfun
def hello(kkk):
    return "Hello "+kkk
print(hello("Gera, "))