# from collections import deque
""" The deque import allows us to have constant time O(1) when dealing with our queue structure """
class Queue():
    def __init__(self, size) :
        # self.data = deque()
        self.data = []
        self.size = size

    def add(self, item):
        if len(self.data) < self.size:
            self.data.append(item)
            return self.data
        else:
            print(f'Queue can\'t exceed {self.size}')

    def remove(self):
        if self.data:
            self.data.pop(0) # removes left most item [first item in queue]
        else:
            print('There is nothing to pop')

    def output(self):
        return self.data

#Test cases
myqueue = Queue(size=10)
myqueue.add(7)
myqueue.add(32)
myqueue.remove()
myqueue.remove()

myqueue.add(1)
myqueue.add(2)
myqueue.add(3)
myqueue.add(4)
myqueue.add(5)
myqueue.add(6)

myqueue.remove()

print(myqueue.output())