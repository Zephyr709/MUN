# Assignment 1

## COMP2001, Fall 2023

### Due: September 25, 2023 @ 11:00pm

Assume that a bank maintains a credit card account for each customer. The credit card account offers convenience to users by allowing them to make purchases without having to carry cash, and by allowing them to pay the balance within a certain duration without incurring any fines. Each purchase or pay balance can be considered as a transaction.

Create two classes: CreditCard and Transaction.

The CreditCard class should store the following information for each customer:

- Customer name (a String)

- Account number (a String)
- Balance (a float)
- Credit limit (a float)
- Credit available (a float)
- Transaction history (a List of Transaction objects, can use ArrayList)

The CreditCard class should have the following member functions:

- A Constructor that takes in parameters to initialize customerName, accountNumber, creditLimit fields.

- public void purchase (float amount, String source): Make a purchase transaction for the specified amount and with the transaction vendor indicated by the source parameter. The function should update the balance and credit available accordingly, and should add a new Transaction object to the transaction history.

- public void payback (float amount): Pay back an amount to the account. The transaction vendor should be indicated as "Payback". The function should update the balance and credit available accordingly, and should add a new Transaction object to the transaction history with the vendor set to "Payback".
  
- public void printHistory(): Print a string representation of the transaction history.
Get accessors and set mutators for the class attributes.

- An additional member function that you think would be interesting or useful.
  
The Transaction class should have the following fields:

- Source (the vendor for the transaction, a String)
  
- Transaction date (a Date object)
- Amount (a float)
- Purchase type (either "Purchase" or "Payback", a String)
- The Transaction class should have necessary member functions including constructors.
- The Transaction class should have accessors and mutators for its fields.
