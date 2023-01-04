""" Stacks are self explanatory, you stack data elements on top of each other,
And the very top data element will have a pointer, 
adding items to a stack is called PUSH, 
removing items is called POP """

class Stack():
    def __init__(self):
        self.data = []
        self.pointer = -1

    def push(self, item):
        self.data.append(item)
        self.pointer += 1
        
    def pop(self):
        self.data.pop() #pop method removes last item in array
        self.pointer -= 1

    def output(self):
        if len(self.data) <= 0:
            return('Your stack is empty')
        for i in self.data:
            print(f"{i}")

    def get_top(self):
        result = self.data[self.pointer]
        return(result)

# Test Cases
mystack = Stack()
mystack.push(5)
mystack.push(3)
mystack.push(4)
mystack.push(7)
mystack.pop()
print(mystack.output())
