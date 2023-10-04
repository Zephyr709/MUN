class LinkedList():
    
    class _Node:
        def __init__(self, element):
            self._element = element
            self._next = None

            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def first_element(self):
        return self._head._element #type: ignore
    
    def is_empty(self):
        return self._head == None

    def add_first(self, e):
        node = self._Node(e)
        node._next = self._head # type: ignore
        
        # if list is empty, the head and tail point to the same node
        if self.is_empty():
            self._tail = node
            
        self._head = node
        self._size += 1
        

    def delete_first(self):
        if self.is_empty():
            raise Exception("Linked List is empty!")
        node = self._head
        self._head = self._head._next # type: ignore
        node = None
        self._size -= 1
        
        
    def add_last(self, e):        
        if self.is_empty():
            # if list is empty, then this case is equivalent to add_first()
            self.add_first(e)
        else:
            # set _next pointer of current tail node to point to the new node
            # and set the new node as the tail
            node = self._Node(e)
            self._tail._next = node # type: ignore
            self._tail = node
        self._size += 1
        
    def findSecondLast(self):
        curr = self._head
        prev = None
        
        while curr._next != None: # type: ignore
            prev = curr
            curr = curr._next # type: ignore
        
        print(prev._element) # type: ignore
        return prev 
        
    def concatenate(self, other):
        currL = self._head
            
        while currL._next!= None: # type: ignore
            currL = currL._next # type: ignore
                
        currL._next = other._head # type: ignore
            
        print("Your Linked list has been concatenated!")
            
        # Time complexity: O(n).

    def __len__(self):
        curr = self._head
        count = 1
        while curr._next!= None: # type: ignore
            count += 1
            curr = curr._next # type: ignore

        return count
    
    def recurLen(self):
        if self.is_empty():
            return 0
        if self._head._next == None: # type: ignore
            return 1
        
        return None

    



def main():
    l = LinkedList()
    l.add_first(1)
    l.add_first(2)
    l.add_first(3)
    l.add_first(4)
    l.add_first(5)
  
    
    m = LinkedList()
    m.add_first(6)
    m.add_first(7)
    m.add_first(8)
    m.add_first(9)
    m.add_first(10)
    
    l.findSecondLast()
    print(l.first_element())
    l.concatenate(m)
    l.findSecondLast()
    print(l.first_element())
    
    print(len(l))
    
    
main()
    
    
    
            
            
                
            
            
            
            
            
            
      