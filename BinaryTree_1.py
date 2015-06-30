__author__ = 'Elias Haroun'

from Lists.ArrayList import *

class BinaryTree(object):

    def __init__(self):
        self.arrayList = ArrayList()
        self.arrayList.insert(0,None)
        self.size = 0
        self.rootIndex = 0

    def getSize(self):
        return  self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, aValue):
        if self.isEmpty():
            self.rootIndex = 1
            self.arrayList.insert(self.rootIndex, aValue)
        elif (self.arrayList.get(self.rootIndex*2)) is None:
            self.arrayList.insert(self.rootIndex*2, aValue)
        elif (self.arrayList.get(self.rootIndex*2+1)) is None:
            self.arrayList.insert(self.rootIndex*2+1, aValue)
            self.rootIndex += 1

        self.size += 1

    def delete(self):
        return 0

    def getContent(self):
        result = []
        for i in range (self.arrayList.capacity):
            #if self.arrayList.get(i) is not None:
            result.append(self.arrayList.get(i))
        print (result)

    def hasLeft(self, index):
        return (self.arrayList.get(index*2) is not None)

    def hasRight(self, index):
        return (self.arrayList.get(index*2+1) is not None)

    def isLeaf(self, index):
        return not (self.hasRight(index) | self.hasLeft(index))

    def preOrder(self, rootIndex):
        if self.isEmpty():
            return None
        elif self.isLeaf(rootIndex):
            print(self.arrayList.get(rootIndex))
        else:
            print(self.arrayList.get(rootIndex))
            if self.hasLeft(rootIndex):
                self.preOrder(rootIndex*2)
            if self.hasRight(rootIndex):
                self.preOrder(rootIndex*2+1)

    def postOrder(self, rootIndex):
        if self.isEmpty():
            return None
        elif self.isLeaf(rootIndex):
            print(self.arrayList.get(rootIndex))
        else:
            if self.hasLeft(rootIndex):
                self.postOrder(rootIndex*2)
            if self.hasRight(rootIndex):
                self.postOrder(rootIndex*2+1)
            print(self.arrayList.get(rootIndex))

    def inOrder(self, rootIndex):
        if self.isEmpty():
            return None
        elif self.isLeaf(rootIndex):
            print(self.arrayList.get(rootIndex))
        else:
            if self.hasLeft(rootIndex):
                self.inOrder(rootIndex*2)
            print(self.arrayList.get(rootIndex))
            if self.hasRight(rootIndex):
                self.inOrder(rootIndex*2+1)