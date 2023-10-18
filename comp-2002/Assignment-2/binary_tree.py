# Name: Jager Cooper
# Student ID: 201765344
#
# COMP 2002
# October, 2023

class BinaryTree():

    def __init__(self):
        self._data = [None]


    def is_empty(self):
        return len(self._data) <= 1

    def root(self):
        """ Returns the value of the root node. """
        if self.is_empty():
            return None
        else:
            return self._data[1]

    def inorder_traversal(self):
        """ Prints an inorder traversal of the tree. """
        print("Inorder Traversal: ", end='')
        if not self.is_empty():
            print(str(self._inorder_helper(1)))
        else:
            print('[]')

    def _inorder_helper(self, index):
        """ Recursive private method to implement inorder traversal. """
        left_index = 2 * index
        right_index = 2 * index + 1
        traversal = []
        if left_index < len(self._data) and self._data[left_index]:
            traversal += self._inorder_helper(left_index)
        traversal += [self._data[index]]
        if right_index < len(self._data) and self._data[right_index]:
            traversal += self._inorder_helper(right_index)
        return traversal

    def preorder_traversal(self):
        """ Prints a preorder traversal of the tree. """
        print("Preorder Traversal: ", end='')
        if not self.is_empty():
            print(str(self._preorder_helper(1)))
        else:
            print('[]')

    def _preorder_helper(self, index):
        """ Recursive private method to implement preorder traversal. """
        left_index = 2 * index
        right_index = 2 * index + 1
        traversal = [self._data[index]]
        if left_index < len(self._data) and self._data[left_index]:
            traversal += self._preorder_helper(left_index)
        if right_index < len(self._data) and self._data[right_index]:
            traversal += self._preorder_helper(right_index)
        return traversal

    def postorder_traversal(self):
        """ Prints a postorder traversal of the tree. """
        print("Postorder Traversal: ", end='')
        if not self.is_empty():
            print(str(self._postorder_helper(1)))
        else:
            print('[]')

    def _postorder_helper(self, index):
        """ Recursive private method to implement postorder traversal. """
        left_index = 2 * index
        right_index = 2 * index + 1
        traversal = []
        if left_index < len(self._data) and self._data[left_index]:
            traversal += self._postorder_helper(left_index)
        if right_index < len(self._data) and self._data[right_index]:
            traversal += self._postorder_helper(right_index)
        traversal += [self._data[index]]
        return traversal

    def read_string(self, s):
        """ Creates a tree given a string representation.

        For example, s could be '1, 2, 3, None, 4'.

        1 is the root node, with 2 and 3 its left and right children.
        2 has no left child, but a right child with value 4.
        3 has no children."""

        # TO DO: Question 1.



    def boundary_traversal(self):
        """ Prints a boundary traversal of the tree. """

         # TO DO: Question 2


