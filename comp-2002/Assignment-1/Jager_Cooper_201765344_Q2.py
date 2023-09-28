# Jager Cooper
# 201765344

# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Basic example of an adapter class to provide a stack interface to Python's list."""

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data.pop()               # remove last item from list
  
  
  
  def __eq__(self,other):
    """
    implements the == operation.
    
    returns true if the current stack contains the same contents, in the same order as the other stack, otherwise false. 
    
    does not modify this stack or the other stack 
    """
    if len(self._data) != len(other._data):
      return False
    
    for i in range(0,len(self._data)):
      if self._data[i] != other._data[i]:
        return False
    
    return True
  
  def __ne__(self,other):
    """
    implements the != operation. 
    
    returns true if the contents of the two stacks are different or in a different order, otherwise false.
    
    does not modify this stack or the other stack.
    """
    
    if len(self._data) != len(other._data):
      return True
    
    for i in range(0,len(self._data)):
      if self._data[i] != other._data[i]:
        return True
    
    return False
  
  def __iadd__(self,other):
    """
    implements the += operation. 
    
    adds the contents of a second stack, other, onto the top of the current stack and returns the combined stack. 
    
    does not modify the other stack.
    """
    for element in other._data:
      self._data.append(element)
    
    return
  
  def __str__(self):
    """
    implements the str() operation. 
    
    returns a string representation of the contents of this stack.
    
    the string is formatted as [a, b, c, ...], where a, b, c, etc are the elements stored in the stack, with the top of the stack to the left. 
    
    does not modify the stack.
    """
    strArray = ""
    
    for element in self._data:
      strArray = str(element) + strArray
      
    
    return ("[" + "]")
  
  
def main():
    a = ArrayStack()
    a.push(5)
    a.push(10)
    a.push(15)
    b = ArrayStack()
    b.push(5)
    b.push(10)
    b.push(15)
    print(a == b)
    
    print(a != b)
    
    str(a)
    
    c = ArrayStack()
    c.push(3)
    c.push(2)
    c.push(1)
    print(str(c))
    
    a += c
    print(str(a))
    
    print(str(c))
    
    print(a == c)

main()