

class MyIter(object):
	def __init__(self, l):
		self.l = l
		self.cur_index = 0

        def __iter__(self):
		return self

	def next(self):
		if self.cur_index < len(self.l):
			cur_ele = (self.l)[self.cur_index]
			self.cur_index += 2
			return cur_ele
		raise StopIteration()

class Fab(object):
	def __init__(self, max):
		self.max = max
		self.n, self.a, self.b = 0, 0 ,1

	def __iter__(self):
		return self

	def next(self):
		if self.n < self.max:
			r = self.b
			self.a, self.b = self.a, self.a + self.b
			self.n = self.n+1
			return r
		raise StopIteration()

for k in MyIter([1,2,3,4]):
	print k
