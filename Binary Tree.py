""" So a Binary Tree is a data structure consisting of a parent node,
and each parent has two children nodes, the left child is smaller than its parent,
but the right child is larger.
This allows us to have concrete rules on the building, searching, and tranversing 
of a binary tree. """

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.setnode = None

    def add(self, value):
        node = Node(value)
        if self.setnode is None:
            self.setnode = node
            return
        currentNode = self.setnode
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = node
                    break
                else:
                    currentNode = currentNode.left
            if value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = node
                    break
                else:
                    currentNode = currentNode.right

    def find(self, value):
        if self.setnode.value == value:
            return True
        currentNode = self.setnode
        
    def delete(self):
        pass

    def ouput(self):
        pass

tree = Tree()
tree.add(5)
tree.add(3)
tree.add(2)
tree.add(6)
tree.add(4)

            

    