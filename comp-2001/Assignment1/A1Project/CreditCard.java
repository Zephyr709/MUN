/*
 * Jager Cooper
 * 201765344
 */

import java.util.ArrayList;

public class CreditCard {
    /* Class Attributes */
    private String customerName;
    private String accountNumber;
    private float balance;
    private float creditLimit;
    private float creditAvail;
    private ArrayList<Transaction> transactionHistory;


    /* Constructor */
    public CreditCard(String name, String accountNum, float creditLim) {
        /* Attribute Initialization */
        customerName = name;
        accountNumber = accountNum;
        balance = 0.00f;
        creditLimit = creditLim;
        creditAvail = 0.00f;
        transactionHistory = new ArrayList<>();

    }

    /* Mutator and accessor methods */
    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getAccountNumber() {
        return accountNumber;
    }
    
    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    public float getCreditLimit() {
        return creditLimit;
    }

    public void setCreditLimit(float creditLimit) {
        this.creditLimit = creditLimit;
    }

    public float getCreditAvail() {
        return creditAvail;
    }

    public void setCreditAvail(float creditAvail) {
        this.creditAvail = creditAvail;
    }

    public ArrayList<Transaction> getTransactionHistory() {
        return transactionHistory;
    }

    public void setTransactionHistory(ArrayList<Transaction> transactionHistory) {
        this.transactionHistory = transactionHistory;
    }

    /* Additional Methods */

     public void purchase(float amount, String source) {
        /*
         * This function updates the balance and credit available based upon a purchase 
         * transaction and creates a transaction object.
         */

        balance += amount;
        creditAvail -= amount;
        transactionHistory.add(0, new Transaction(source, amount, "Purchase"));
         

     }

     public void payback(float amount, String source) {
        /*
         * This function updates the balance and credit available based upon a payback
         * transaction and creates a transaction object.
         */

         balance -= amount;
         creditAvail += amount;
         transactionHistory.add(0, new Transaction(source, amount, "Payback"));

         
     }
     
     public void printHistory() {
        /* This Function prints out the transaction history of the credit card */
        for (int i = 0; i < transactionHistory.size(); i++){
            System.out.println(transactionHistory.get(i));
            
        }

     }

     public void cashBackBonus() {
        /* 
         * Generates a 3% cash back bonus based upon transaction history 
         * and adds the refund to the credit card account
        */

        float x = 0.0f;

        for (int i = 0; i < transactionHistory.size (); i++){
            if (transactionHistory.get(i).getPurchaseType() == "Purchase"){
                x += transactionHistory.get(i).getAmount();
            }
            
        /* Calculates the cash back bonus and applies it to the account */
        float bonus = x * 0.03f;
        balance -= bonus;
        creditAvail += bonus;

        System.out.println("Your cash back bonus is: " + bonus);
        
        }


     }
}