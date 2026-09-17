class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedQ:
    def __init__(self):
        self.__first = None 
        self.__last = None  

    def isEmpty(self):
        return self.__first == None

    def enqueue(self, x):
        ny_nod = Node(x)
        
        if self.isEmpty():
            self.__first = ny_nod
            self.__last = ny_nod
        else:
            self.__last.next = ny_nod
            self.__last = ny_nod

    def dequeue(self):
        ut_varde = self.__first.value
        
        self.__first = self.__first.next
        
        if self.__first == None:
            self.__last = None
            
        return ut_varde