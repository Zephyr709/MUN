import java.util.ArrayList;

import java.util.Iterator;

public class Bank {
    
    public String bankName;
    public ArrayList<Account> accounts;

    /**
     * Default Constructor
     */
    public Bank(){
        accounts = new ArrayList<Account>();
        bankName = "N/A";
    }

    /**
     * Constructor with bankName parameter
     * 
     * @param bankName , String : the name of the bank
     */
    public Bank(String bankName){
        accounts = new ArrayList<Account>();
        this.bankName = bankName;
    }

    /**
     * Adds a new account to the bank
     * 
     * @param account , Account : an account to add to the bank
     */
    public void add(Account account){
        accounts.add(account);
    }

    /**
     * Displays the bank name,and the full list of accounts at the bank
     */
    public void display(){
        System.out.println("Bank Name: " + bankName);
        for (Iterator<Account> it = accounts.iterator(); it.hasNext();) {
            Account currentAccount = it.next();

            currentAccount.display();
        }
    }

    /**
     * Displays the bank name, and all accounts associated with the user name 
     * 
     * @param user , String : user name to search owned accounts for
     */
    public void display(String user){
        accounts.stream()
        .filter(account -> account.getUserName().equals(user))
        .forEach(account -> account.display());
    }
}
