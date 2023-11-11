
# Assignment 3 Instructions

## COMP2001, Fall 2023

### Due: November 16, 2023 @ 11:00pm

Assume that a bank maintains three types of accounts for each customer: credit, savings, and checking. The credit card account offers users the convenience of making purchases without having to carry cash and allows them to pay the balance within a specified duration without incurring a fine. The savings account provides compound interest and withdrawal facility, while the checking account offers a cheque book facility but no interest.

#### For this assignment, create a class called Account that stores customer account number, user name, and balance. It is recommended to use protected for the variable balance. The Account class should have the following member functions

- Account(): the default constructor that generates an account number using a random integer and initializes other member variables.

- Account(String user): the overloaded constructor that takes the argument for the account name and initializes other member variables.

- void display(): displays (prints) the account information, including the user name, account number, and the balance.

- void deposit(float m): accepts a deposit from a customer and updates the balance.

- void withdraw(float m): defines an abstract method that can be overridden by the derived class and enables late dynamic calling of corresponding member functions in the derived classes.

- float getBalance(): returns the balance.

- String getUserName(): returns the user name.

#### Create two derived classes from the Account class: Cheque and Saving. In the Cheque class, declare private static final member variables minimBalance and overLimitCharge (set to 1000 and 5, respectively). In the Saving class, declare a private static final member variable called eachTimeCharge (set to 3.9) that stores the service rate for each time a withdrawal is made

The Cheque class should have the following member functions:

- Two constructors similar to those of the parent class Account.

- A withdraw function that withdraws money according to the user's request. In this function, check if this withdrawal is allowed according to the available balance and withdraw limit for each time. Calculate the over-limit service fee if the balance is lower than a limit when applying a withdrawal. Update the balance.

The Saving class should have the following member functions:

- Two constructors similar to those of the parent class Account.

- A withdraw function that withdraws money according to the user's request. In this function, check if this withdrawal is allowed according to the available balance for each time. Apply a service fee for each time a withdrawal is made. Update the balance.

#### Create a Bank class to maintain the accounts, which has members bankName and an ArrayList accounts that store checking and saving accounts. The Bank class should have the following member functions

- Bank(): the default constructor that creates a new empty account list (using ArrayList).

- Bank(String name): a constructor with a string argument for the bank name.

- void add(Account a): adds the account (either Saving or Cheque objects).

- void display(): displays the bank name and the full list of accounts (including the user’s name, balance, and the type of account (whether it is Saving or not)).

- void display(String user): displays the bank name and the list of accounts of a specific user name (including the user’s name, balance, and the type of account (whether it is Saving or not)).

#### Finally, test the functionality of the program with the following steps

- Create a saving account with the user name "John," deposit and withdraw money, and display the balance to test the logic.

- Create a checking account with the user name "John," deposit and withdraw money, and display the balance to test the logic.

- Create a bank object and name it "CIBC," add the above two accounts, and display the full list.
Repeat steps 1 and 2 to add more accounts with different names and
