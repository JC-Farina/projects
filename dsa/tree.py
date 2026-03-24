class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printInOrder(root):
    if (root == None):
        return
    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right)

if __name__=='__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    printInOrder(root)
