class Node:
     
   
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
     
    # head nulo por default
    def __init__(self):
        self.head = None
     
    
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    
    def push(self,data):
         
        if self.head == None:
            self.head=Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
     
    
    def pop(self):
         
        if self.isempty():
            return None
             
        else:
            
            popnodo = self.head
            self.head = self.head.next
            popnodo.next = None
            return popnodo.data
     
    
    def peek(self):
         
        if self.isempty():
            return None
             
        else:
            return self.head.data
     
    # Prints out the stack    
    def display(self):
         
        iternode = self.head
        if self.isempty():
            print("Stack vacia")
         
        else:
             
            while(iternode != None):
                 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return