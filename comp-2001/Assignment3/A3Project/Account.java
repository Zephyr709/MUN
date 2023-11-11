import java.util.Random;

class Account {
    protected float balance;
    public int accountNumber;
    public String userName;
    private Random rand = new Random();

    /**
     * Default constructor 
     * Initializes the userName with N/A
     * Initializes the account number with a random integer
     * Initaialzes the balance to 0
     */
    public Account(){
        accountNumber = rand.nextInt();
        balance = 0;
        userName = "N/A";
    }

    /**
     * Parmeterized constructor
     * Initializes the account number with a random integer
     * Initializes the balance to 0
     * Initaialzes the userName with user parameter
     * 
     * @Param String User, the user name to associate with the account
     */
    public Account(String user){
        accountNumber = rand.nextInt();
        balance = 0;
        userName = user;
    }

    /**
     * Prints out all the details associated with the account
     * 
     */
    public void display(){
        System.out.println("User name: " + userName);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: " + balance);
        System.out.println();
    }

    /**
     * Processes a deposit into the account
     * 
     * @param m a float amount to deposit to the account
     */
    public void deposit(float m){

    }

    /**
     * process a withdraw from the account
     * 
     * @param m a float amount to withdraw from the account
     */
    public void withdraw(float m){

    }

    /**
     * Gets the current balance of the account and returns it.
     * 
     * @return Float, the current balance of the account
     */
    public float getBalance(){
        return balance;
    }

    /**
     * Gets the user name of the account and returns it.
     * 
     * @return String, the user name associated with the account
     */
    public String getUserName(){
        return userName;
    }
}