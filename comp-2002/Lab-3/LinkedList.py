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
        return self._head._element
    
    def is_empty(self):
        return self._head == None

    def add_first(self, e):
        node = self._Node(e)
        node._next = self._head
        
        # if list is empty, the head and tail point to the same node
        if self.is_empty():
            self._tail = node
            
        self._head = node
        self._size += 1
        

    def delete_first(self):
        if self.is_empty():
            raise Exception("Linked List is empty!")
        node = self._head
        self._head = self._head._next
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
            self._tail._next = node
            self._tail = node
        self._size += 1
        