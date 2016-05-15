class Node(object):
    """docstring for Node"""
    def __init__(self, item, left, right):
        super(Node, self).__init__()
        self.item = item
        self.left = left
        self.right = right

    def getChild(self, direction):
        if (direction > 0):
            return self.left
        else:
            return self.right

    def getItem(self):
        return self.item

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def isLeaf(self):
        return (self.left is None) and (self.right is None)

    def setChild(self, direction, child):
        if (direction > 0):
            self.left = child
        else:
            self.right = child

    def setItem(self, item):
        self.item = item

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def toStringInorder(self):
        result = ""
        if (self.left != None):
            result += "\n" + self.left.toStringInorder()

        result += self.item + "\n"

        if (self.right != None):
            result += "\n" + self.right.toStringInorder()

        return result
