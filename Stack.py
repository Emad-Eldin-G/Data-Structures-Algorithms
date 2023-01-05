""" Stacks are self explanatory, you stack data elements on top of each other,
And the very top data element will have a pointer, 
adding items to a stack is called PUSH, 
removing items is called POP """

class Stack1():
    def __init__(self):
        self.data = []
        self.pointer = -1
        # self.size = size (where a user will specify the size of his data)

    def push(self, item):
        if len(self.data) < 10:
            self.data.append(item)
            self.pointer += 1
        else:
            print ('Stack is full')
            
    def pop(self):
        if self.data:
            self.data.pop() #pop method removes last item in array
            self.pointer -= 1
        else:
            'Stack is empty'

    def output(self):
        if len(self.data) <= 0:
            return('Your stack is empty')
        for i in self.data:
            print(f"{i}")

    def get_top(self):
        result = self.data[self.pointer]
        return(result)

#_____________________________________________________

class Stack2():
    def __init__(self):
        self.data = [None for i in range(10)]
        self.pointer = -1

    def push(self, item):
        for x, y in enumerate(self.data):
            if y == None:
                self.data[x] == item
                self.pointer += 1
            elif self.pointer >= 10:
                print ('Stack is full')
                
    def pop(self):
        try:
            for x, item in enumerate(self.data):
                if item == None:
                    self.data[x-1] = None
        except Exception:
            print('Stack already empty') #pop method removes last item in array
        self.pointer -= 1

    def output(self):
        return self.data

    def get_top(self):
        result = self.data[self.pointer]
        return(result)

# Test Cases
mystack = Stack1()
mystack.push(7)
mystack.push(32)
mystack.push(1)
mystack.pop()
mystack.pop()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.push(6)
mystack.push(7)
mystack.push(8)
mystack.push(9)
mystack.push(10)
mystack.push(11)
mystack.push(11)
mystack.push(11)
mystack.push(11)

