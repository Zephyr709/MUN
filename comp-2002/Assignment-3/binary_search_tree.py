# COMP 2002
# Student name
# Student ID

class BinarySearchTree():

    class _Item():
        """ No need to modify. This has already been changed to store (x, y) data. """
        def __init__(self, x, y):
            self.x = x
            self.y = y



    class _Node():
        """ Do not modify this class. """

        def __init__(self, parent=None, left=None, right=None, item=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.item = item

        def is_external(self):
            return self.left == None and self.right == None

    def __init__(self):
        """ Do not modify the constructor. """
        self._root = None
        self._size = 0

    def _search(self, p, x, y):
        ## TO DO - Question 2
        ## Currently finds the with item with key, k, in the subtree rooted at p.
        ## Modify for (x, y) positional data

        if k == p.item.key:
            return p
        elif k < p.item.key and p.left is not None:
            return self._search(p.left, k)
        elif k > p.item.key and p.right is not None:
            return self._search(p.right, k)
        return p


    def search(self, x, y):
        ## TO DO - Question 2
        ## Currently finds the item with key, k.
        ## Modify for (x, y) positional data.

        return self._search(self._root, k)


    def insert(self, x, y):
        ## TO DO - Question 2
        ## Currently inserts a new item with key-value pair k,v.
        ## Modify for (x, y) positional data.

        if self._root is None:
            item = self._Item(k, v)
            self._root = self._Node(item=item)
        else:
            p = self.search(k)
            if k == p.item.key: # will update this item with new value
                p.item.value = v
            elif k < p.item.key:
                item = self._Item(k, v)
                c = self._Node(parent=p, item=item)
                p.left = c
            else:
                item = self._Item(k, v)
                c = self._Node(parent=p, item=item)
                p.right = c


    def find_nearby_vertexes(self, x_centre, y_centre, radius):
        """ Returns a list of points, each as (x, y) tuple pairs, that are within the
            circle with given radius centred on position (x_centre, y_centre). """

        ## TO DO - Question 3