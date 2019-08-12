from Node import Node

class ListStack():
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def clear(self):
        self.top = None
    
    def push(self, data):
        self.top = Node(data, self.top)
    
    def pop(self):
        if self.isEmpty():
            return False
        top_info = self.top.item
        self.top = self.top.next_node
        return top_info
    
    def peek(self):
        if self.isEmpty():
            return False
        return self.top.item
    
    def __str__(self):
        if self.isEmpty():
            return False
        stack_text = []
        temp = self.top
        while temp:
            stack_text.append(temp.item)
            temp = temp.next_node
        return str(stack_text)

        
            