# -*- coding: utf-8 -*-

def show(show_type):
	def to_show(func):
		""" func 为被装饰的函数对象 """
		def inner_func(*args, **kwargs):
			""" inner_func 用来预处理我们想做的事 """
			if show_type == 'name':
				print 'func name is: %s' % func.__name__
			else:
				print 'func doc: %s' % func.__doc__

			func(*args, **kwargs)  # 执行被装饰函数func
			return
		return inner_func  # 把包装好的函数对象返回出去
	return to_show


@show('name')
def add(a, b):
	print(a+b)

@show('blabla')
def div(a, b):
	"""division function"""
	print(a/b)

add(1,2)
div(10,5)
