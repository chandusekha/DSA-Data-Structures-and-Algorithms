class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Statck:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.length=1

    def push(self,value):
        new_node=Node(value)
        if self.length==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.length+=1
        return True

    def pop(self):
        if self.length==0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.length-=1
        return temp
            

    def print_list(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
        

S=Statck(5)
S.push(45)
S.print_list()
S.push(115)
S.print_list()
S.pop()
S.pop()
S.print_list()


