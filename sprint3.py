def wrap(pre, post):

    def decorate(func):

        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)
            print(args)
            return result

        print(call)
        return call

    print(decorate)
    return decorate


def trace_in(func, *args, **kwargs):
   print("Entering function",  func.__name__)

def trace_out(func, *args, **kwargs):
   print("Leaving function", func.__name__)

@wrap(trace_in, trace_out)
def calc(x, y):
   return calc2(x+y)

@wrap(trace_in, trace_out)
def calc2(z):
	return 2*z

def main():
	
	print(calc(1,4))

main()