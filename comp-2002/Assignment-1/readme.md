# Comp 2002 - Assignment 1 (4%)

## Due: 11:59pm, Tuesday, Oct. 3, 2023

## Learning Objectives

the goal of this assignment is to gain experience with recursion and stacks.

### Question 1: (30 pts)

implement a recursive functionL named question1(). that computes the mathematical function
below.

𝑓 (𝑚, 𝑛, 𝑝) =

𝑚 + 𝑝 for 𝑛 < 1

𝑚 +𝑛 for 𝑝 < 1

𝑓 (𝑚, lg(𝑛), lg(𝑝)) + 𝑓 (𝑚, 𝑛/2, 𝑓 (𝑚, 𝑛, lg(𝑝))) otherwise

for example: input values 𝑚 =5L 𝑛 =4L 𝑝 =3 have an output value of 144.546292.

### Question 2: (70 pts)

python classes have a number of methods with special names. we have seen one example of this
already in this course: __init__() is the constructor for a class.

implement the following special methods in the provided ArrayStack classN follow proper
programming etiquette - do not access private methods or variables of other objects.

#### __eq__(self, other)

- implements the == operation. returns true if the current stack contains the same contents, in
the same order as the other stack, otherwise false. does not modify this stack or the other
stack

#### __ne__(self, other)

- implements the != operation. returns true if the contents of the two stacks are different or in a
different order, otherwise false, does not modify this stack or the other stack.

#### __iadd__(self, other)

- implements the += operation. adds the contents of a second stack, other, onto the top of the
current stack and returns the combined stack, does not modify the other stack.

#### __str__(self, other)

- implements the str() operation. returns a string representation of the contents of this stack.
the string is formatted as [a, b, c, ...], where a, b, c, etc are the elements stored in the
stack, with the top of the stack to the left. does not modify the stack.

#### Example

``` python
>>> a = ArrayStack()
>>> a.push(5)
>>> a.push(10)
>>> a.push(15)
>>> b = ArrayStack()
>>> b.push(5)
>>> b.push(10)
>>> b.push(15)
>>> a == b
True
>>> a != b
False
>>> str(a)
’[15, 10, 5]’
>>> c = ArrayStack()
>>> c.push(3)
>>> c.push(2)
>>> c.push(1)
>>> str(c)
’[1, 2, 3]’
>>> a += c
>>> str(a)
’[1, 2, 3, 15, 10 5]’
>>> str(c)
’[1, 2, 3]’
>>> a == c
False
```
