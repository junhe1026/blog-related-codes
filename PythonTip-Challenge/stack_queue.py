# -*- coding: utf-8 -*-

"""两个栈实现一个队列"""


class SQueue(object):
    """用2个栈实现一个队列, 用List模拟栈"""

    def __init__(self, *args):
        if len(args) > 1:
            raise Exception('only take 0 or 1 arg')
        self.s1 = Stack(args[0])  # 只用来存
        self.s2 = Stack()  # 只用来取

    def enqueue(self, ele):
        self.s1.push(ele)

    def dequeue(self):
        if not self.s2:
            # 如果s2没有元素，把s1的都放入s2,再取
            while self.s1:
                self.s2.push(self.s1.pop())
        try:
            return self.s2.pop()
        except ValueError:
            raise ValueError('Queue is empty')

    def __str__(self):
        return '->'.join([str(self.s1), str(self.s2)])

    def __len__(self):
        return len(self.s1)+len(self.s2)


class Stack(object):
    """用list实现简单的stack"""

    def __init__(self, *args):
        if len(args) > 1:
            raise Exception('only take 0 or 1 arg')
        if not args:
            self.stack = list()
        elif isinstance(args[0], list):
            self.stack = args[0]
        else:
            self.stack = list(args[0])

    def __repr__(self):
        return "List base stack"

    def __str__(self):
        if not self.stack:
            return ''
        return '->'.join([str(i) for i in self.stack])

    def __len__(self):
        return len(self.stack)

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if self.stack:
            last = self.stack[-1]
            self.stack = self.stack[:-1]
            return last
        else:
            raise ValueError('stack is empty')

if __name__ == '__main__':
    # s = Stack()
    # print(s)
    # s.push(4)
    # print(s)
    # print(s.pop())
    # print(s)

    # SQueue
    q = SQueue(['1', '2'])
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print(str(q))
    print('get:', q.dequeue())
    print(q.dequeue())
    q.enqueue('d')
    print(q.dequeue())
    print(str(q))



