__author__ = 'Elias Haroun'

from BinaryTree_ADT.tree.list.BinaryNode import *

class BinaryTree(object):

    def __init__(self):
        self.size = 0;
        self.root = None

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def getRoot(self):
        return self.root

    def setRoot(self, aNode):
        self.root = aNode

    def add(self, data, binaryNode):
        if data < binaryNode.data:
            if binaryNode.getLeft() is not None:
                self.add(data, binaryNode.getLeft())
            else:
                binaryNode.setLeft(BinaryNode(data))
        else:
            if binaryNode.getRight() is not None:
                self.add(data, binaryNode.getRight())
            else:
                binaryNode.setRight(BinaryNode(data))