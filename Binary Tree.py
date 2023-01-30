""" So a Binary Tree is a data structure consisting of a parent node,
and each parent has two children nodes, the left child is smaller than its parent,
but the right child is larger.
This allows us to have concrete rules on the building, searching, and tranversing 
of a binary tree. """

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self) -> None:
        self.setnode = None

    def add(self, value):
        node = Node(value)
        if self.setnode is None:
            self.setnode = node
        currentNode = self.setnode
        if currentNode.left is not None or currentNode.right is not None:
            if value < currentNode.value:
                currentNode.left = node
            if value > currentNode.value:
                currentNode.right = node
        else:
            if value < currentNode.value:
                currentNode.left = node
            if value > currentNode.value:
                currentNode.right = node

    def delete(self):
        pass

    def ouput(self):
        pass

            

    