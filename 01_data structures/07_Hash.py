class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size
    
    def __hash(self,key):
        myhash=0
        for letter in key:
            myhash=(myhash+ord(letter)*23 )% len(self.data_map)
        return myhash

    def set_items(self,key,value):
        index=self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for x in range(len(self.data_map[index])):
                if self.data_map[index][x][0]==key :
                    return self.data_map[index][x][1]
        return None

    def keys(self):
        all_keys=[]
        for x in range(len(self.data_map)):
            if self.data_map[x] is not None:
                for i in range(len(self.data_map[x])):
                    all_keys .append(self.data_map[x][i][0])
        return all_keys

    def print_hash(self):
        for i,j in enumerate(self.data_map):
            print(i ," : ", j)
    

ht1=HashTable()
ht1.print_hash()
ht1.set_items('nuts',2000)
ht1.set_items('screws',1100)
ht1.set_items('nails',500)
ht1.set_items('noze',5010)

ht1.print_hash()
print(ht1.get('mose'))

ht1.keys()
# --------------------------------------Challenge----------------------------------------------------

def commom_items(list1,list2):
    my_dict={}
    for i in (list1):
        my_dict[i]=True
    
    for j in (list2):
        if j in my_dict:
            return j
    return False
    
list1=[1,6,3]
list2=[2,4,5]

print(commom_items(list1,list2))