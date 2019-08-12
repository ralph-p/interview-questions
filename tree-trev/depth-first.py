import Queue
import random

class Node():
    def __init__(self,data):
        self.data = data
        self.children = []
    
    def add_child(self,child):
        self.children.append(child)
    def set_children(self,child_arr):
        self.children = child_arr
    def get_data(self):
        return self.data



def depth_first(root):
    print(root.get_data())
    for c in root.children:
        q.put(c)
    if not q.empty():
        depth_first(q.get())
    else:
        return True

if __name__ == "__main__":
    q = Queue.Queue()
    root = Node("Root")
    for i in range(0,random.randint(0,5)):
        root.add_child(Node("0 Child: " + str(i)))
    for i,child in enumerate(root.children):
        for x in range(0,random.randint(0,5)):
            child.add_child(Node(str(i) + " Child: "+str(x)))

    depth_first(root)
