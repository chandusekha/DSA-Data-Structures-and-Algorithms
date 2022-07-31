

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
        self.length-=1
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<(self.length/2):
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp


    def set_value(self,index,value):
        if index<0 or index>=self.length:
            return None
        temp=self.get(index)
        temp.value=value
        return True

    def insert(self,index,value):
        
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index)  
        pre=temp.prev

        pre.next=new_node
        temp.prev=new_node
        new_node.next=temp
        new_node.prev=pre   
        self.length+=1
        return True  
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        
        before=temp.prev
        after=temp.next

        before.next=after
        after.prev=before
        self.length-=1
        return True

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

        

        
 
dll=DoubleLinkedList(10)
dll.append(124)
dll.append(54)
dll.print_list()
dll.pop()
dll.print_list()
dll.pop()
dll.print_list()
dll.pop()
dll.print_list()
dll.pop()
dll.print_list()
dll.prepend(555)
dll.prepend(42)
dll.print_list()
dll.prepend(21)
dll.print_list()
dll.prepend(111)
dll.print_list()
dll.pop_first()
dll.print_list()
dll.get(2)
dll.set_value(3,1201)
dll.print_list()
dll.insert(3,2522)
dll.print_list()
dll.remove(2)
dll.print_list()