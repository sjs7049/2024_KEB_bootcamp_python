# def out_func(nout):
#     def inner_func(nin):
#         return nout * nout
#     return inner_func(nout)

def out_func(nout):
    def inner_func():
        return nout * nout
    return inner_func

x = out_func(9)
print(type(x))
print(x)
print(x())