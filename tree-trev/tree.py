class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inOrder(r):
    if r:
        inOrder(r.left)
        print(r.data)
        inOrder(r.right)

def preOrder(r):
    if r:
        print(r.data)
        preOrder(r.left)
        preOrder(r.right)

def postOrder(r):
    if r:
        postOrder(r.left)
        postOrder(r.right)
        print(r.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("InOrder: ")
inOrder(root)
print("PreOrder: ")
preOrder(root)
print("PostOrder: ")
postOrder(root)