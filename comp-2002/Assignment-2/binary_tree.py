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
        valList = s.split(", ")
        
        for i in range(len(valList)):
            if (self.somethingNotNone(valList[i:])== False):
                # if all values are "None" break loop - implmented this to avoid bugs in boundary traversal.
                break     
            elif valList[i] == 'None':
                self._data.append(None)
            else:
                self._data.append(valList[i])

   
    def somethingNotNone(self,someList):
        """This function is used to check if a list of strings that represents a binary tree contains a value other than 'None'

        Args:
            someList (List): A subset of the list generated from a passed along string used to build a binary tree

        Returns:
            Boolean : Returns True if there is an item in the list other than 'None'
        """
        for item in someList:
            if item != 'None':
                return True
            
        return False
        
    def boundary_traversal(self):
        """ Prints a boundary traversal of the tree. """

        # TO DO: Question 2
        
        """
        The following two while loops determines the filled size of the binary tree that is represented in data, and then fills each possible node of the tree with None to make it square.
        
        Making the binary tree complete and square does not change what is represented by the data, but makes it the proper format so that the following algorithm does not encounter any issues.
        """
        x = 0
        while (2**x) < len(self._data):
            x += 1
        while len(self._data) < (2**x):
            self._data.append(None)
        
        
        # The following block of code traverses the left side of the binary tree
        i = 1
        valList = []
       
        while i < (len(self._data)/2):
            if self._data[i] != None:
                valList.append(self._data[i])
            i = i*2
        
        # The following block of code traverses the bottom of the binary tree.
        i = int(len(self._data)/2)
        while i < len(self._data):
            if self._data[i] != None:
                valList.append(self._data[i])
            i += 1
        
        # The following block of code traverses the right side of the binary tree.
        i = len(self._data)-1
        while i > 1:

            if self._data[i] != None:
                valList.append(self._data[i])
            i = int(( (i+1)/2 )-1)
            
        print("Boundary Traversal: ", valList)
                
            
                

def main():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree3 = BinaryTree()
    
    testStr1 = "1, 2, 3, None, 4"
    tree1.read_string(testStr1)
    tree1.preorder_traversal()
    
    
    testStr2 = "1, 2, 3, None, 4, None, None, None, None, None, None"
    
    tree2.read_string(testStr2)
    tree2.preorder_traversal()
    
    testStr3 = "1, 2, 3, 4, 5, 6, 7, 8, None, 9, 10, None, 11, None, None"
    
    tree3.read_string(testStr3)
    tree3.preorder_traversal()
    print("Test String 1:", testStr1)
    tree1.boundary_traversal()
    print("Test String 2:", testStr2)
    tree2.boundary_traversal()
    print("Test String 3:", testStr3)
    tree3.boundary_traversal()
    testStr4 = "1, 2, 3, 4, None, 6, None, None, 8, None, 9, None"
    tree4 = BinaryTree()
    tree4.read_string(testStr4)
    print("Test String 4:", testStr4)
    tree4.boundary_traversal()
    
    
if __name__ == "__main__":
    main()