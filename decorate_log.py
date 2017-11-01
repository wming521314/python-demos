#coding: utf-8

import functools

#日志函数不带参数，只在执行之前打印日志
def log0(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#日志函数不带参数，在函数执行前后都打印日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        func_tmp = func(*args, **kw)
        print('end call')
        return func_tmp
    return wrapper

#日志函数带参数，在执行前后打印参数
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            print('%s %s():' % (text, func.__name__))
            func_tmp = func(*args, **kw)
            print('end call')
            #print('func_tmp = %s' % func_tmp)
            return func_tmp
        return wrapper
    return decorator

@log
def foo():
	print("function execute")
	return 666
	
if __name__ == "__main__":
	re = foo();
	print(re)
