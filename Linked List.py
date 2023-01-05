
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node 
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next

    def output(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=' -> ')
            currentNode = currentNode.next
        print('None')

mylist = LinkedList()
mylist.insert('3')
print(mylist.output())
mylist.insert('5')
print(mylist.output())
mylist.insert('8')
print(mylist.output())
