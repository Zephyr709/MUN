import java.util.ArrayList;

public class CreditCard {
    /*Class Attributes */
    private String customerName;
    private String accountNumber;
    private float balance;
    private float creditLimit;
    private float creditAvail;
    private ArrayList<Transaction> transactionHistory;


    /*Constructor */
    public CreditCard(String name, String accountNum, float creditLim) {
        /*Attribute Initialization */
        customerName = name;
        accountNumber = accountNum;
        balance = 0.00f;
        creditLimit = creditLim;
        creditAvail = 0.00f;
        transactionHistory = new ArrayList<>();

    }

    /*
     * Mutator and accessor methods below
     */
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

    /*
     * Additional Methods
     */

     
}