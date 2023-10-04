class DoublyLinkedList:

    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer # type: ignore
        self._trailer._next = self._header # type: ignore
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size
    

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def add_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)


    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def delete_first(self):
        self._delete_node(self._header._next)

    def delete_last(self):
        self._delete_node(self._trailer._prev)
        
    def findMiddleNode(self):
        headEnd = self._header._next
        tailEnd = self._trailer._prev 
        if headEnd == tailEnd:
                return headEnd
            
        while True:
            headEnd = headEnd._next # type: ignore
            if headEnd == tailEnd:
                return headEnd
            
            tailEnd = tailEnd._prev # type: ignore
            if headEnd == tailEnd:
                return headEnd
            
    
            