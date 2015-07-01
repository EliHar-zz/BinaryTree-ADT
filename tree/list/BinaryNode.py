__author__ = 'Elias Haroun'

class BinaryNode(object):

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self, aNode):
        self.left = aNode

    def setRight(self, aNode):
        self.right = aNode

    def hasLeft(self):
        return self.getLeft() is not None

    def hasRight(self):
        return self.getRight() is not None

    def isLeaf(self):
        return not(self.hasLeft() | self.hasRight())

