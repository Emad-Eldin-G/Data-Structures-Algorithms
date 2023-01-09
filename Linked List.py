
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


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
            if currentNode.next is None or currentNode.next.value is None:
                currentNode.next = node
                currentNode.next.previous = currentNode
                break
            currentNode = currentNode.next

    def delete(self, value):
        if self.head is None:
            return ' Your Linked List is empty '
        current = self.head
        while True:
            if current.value == value and current.next is None:
                current.value = None
                del current
                break
            elif current.value == value and current.next is not None:
                current.previous.next = current.next
                current.next.previous = current.previous
                del current
                break
            current = current.next

    def output(self):
        currentNode = self.head
        if self.head is None:
            return 'Your LinkedList is empty'
        while currentNode is not None:
            print(currentNode.value, end=' -> ')
            currentNode = currentNode.next
        return


# Test Cases:


mylist2 = LinkedList()
mylist2.insert(2)
mylist2.insert(5)
mylist2.insert(8)
print(mylist2.output())
mylist2.delete(8)
print(mylist2.output())
mylist2.insert(10)
print(mylist2.output())
mylist2.delete(10)
print(mylist2.output())
