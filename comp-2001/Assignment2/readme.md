# Assignment 2

## COMP2001, Fall 2023

### Due: October 26, 2023 @ 11:00pm

Assuming the StockManager class maintains a list of Product objects and their corresponding stock levels for a company, your task is to complete the implementation of the StockManger class.

The StockDemo class has been created to showcase the usage of StockManager and Product objects. You can instantiate a StockDemo object in the bench of BlueJ and run its demo method to test the functionality of the StockManager class. As you develop the StockManager class, this demo should demonstrate increasing functionality.

### The StockManager Class

The StockManager class utilizes an ArrayList object to store Product items. Its addProduct method adds a new product to the collection. The following methods need to be completed: delivery, findProduct, printProductDetails, and numberInStock.

- The delivery method should find the Product with the given ID in the list of products and then call its increaseQuantity method.
- The findProduct method should look through the collection for a product whose id field matches the id argument of this method. If a matching product is found, that Product should be returned as the method's result.  If no matching product is found, return null from the method.
- The printProductDetails method should iterate over the list of products and print the result of calling the toString() method on each.
- The numberInStock method should locate a product in the collection with a matching ID, and return the current quantity of that product. If no product with a matching ID is found, return zero.

### The Product Class

The Product class, which has been provided to you and should not require any modifications, represents each product sold by the company. It records a product's ID, name and the current stock level of that product. The class includes an increaseQuantity method to increase the stock level of that product and a sellOne method to decrease the stock level by one when an item of that product is sold.

### Implementation

1. Implement the printProductDetails method to ensure that you are able to iterate over the collection of Products. Just print out each product using System.out.println method.  Using an Iterator is the preferred approach, but use an integer index variable if you find that easier to understand.

2. Implement the findProduct method. This differs from the printProductDetails method in that it will not necessarily have to examine every product in the collection before a match is found.  For instance, if the first product in the collection matches the product name, iteration can finish and that first Product returned.  On the other hand, it is possible that there might be no match for the name in the collection. In that case, the whole collection will be examined, without finding a product to return.  In this case the null value should be returned.

3. Implement the numberInStock method.  This is relatively simple to implement once the findProduct method has been completed. For instance, numberInStock can call the findProduct method to do the searching, and then call the getQuantity method on the result. Watch out for products that cannot be found, though.

4. Implement the delivery method using a similar approach to that used in numberInStock.

5. Implement a method in StockManager to print details of all products with stock levels below a given value (passed as a parameter to the method). MUST be implemented in functional style (using lambdas and streams).

6. Modify the addProduct method so that a new product cannot be added to the product list with the same ID as an existing one.

7. Add to StockManager a method that finds a product from its name rather than its ID:

        public Product findProduct(String name)
