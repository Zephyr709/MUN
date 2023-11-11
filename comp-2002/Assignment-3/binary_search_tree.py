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

        if x == p.item.x :
            if y == p.item.y:
                return p
            elif y < p.item.y and p.left is not None:
                return self._search(p.left, x,y)
            elif y > p.item.y and p.right is not None:
                return self._search(p.right, x,y)
        elif x < p.item.x and p.left is not None:
            return self._search(p.left, x,y)
        elif x > p.item.x and p.right is not None:
            return self._search(p.right, x,y)
        return p


    def search(self, x, y):
        ## TO DO - Question 2
        ## Currently finds the item with key, k.
        ## Modify for (x, y) positional data.

        return self._search(self._root, x, y)


    def insert(self, x, y):
        ## TO DO - Question 2
        ## Currently inserts a new item with key-value pair k,v.
        ## Modify for (x, y) positional data.

        if self._root is None:
            item = self._Item(x, y)
            self._root = self._Node(item=item)
        else:
            p = self.search(x,y)
            if x == p.item.x: # Prints a message that the vertex already exists
                if y == p.item.y:
                    print('This vertex already exists in the tree.')
            elif x < p.item.x:
                item = self._Item(x, y)
                c = self._Node(parent=p, item=item)
                p.left = c
            else:
                item = self._Item(x, y)
                c = self._Node(parent=p, item=item)
                p.right = c


    def find_nearby_vertexes(self, x_centre, y_centre, radius):
        """ Returns a list of points, each as (x, y) tuple pairs, that are within the
            circle with given radius centred on position (x_centre, y_centre). """

        ## TO DO - Question 3