# from collections import deque
""" The deque import allows us to have constant time O(1) when dealing with our queue structure """
class Queue():
    def __init__(self) -> None:
        # self.data = deque()
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self):
        self.data.popleft() # removes left most item [first item in queue]
