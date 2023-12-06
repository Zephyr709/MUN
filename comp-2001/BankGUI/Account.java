import java.util.Random;

public abstract class Account {

    protected int accountNumber;
    protected String accountName;
    protected double balance;

    private static final Random rand = new Random();

    public Account(String accountName) {

        this.accountName = accountName;
        accountNumber = rand.nextInt(1000000);
        balance = 0.0;

    }

    public Account(String accountName, double balance) {
        this(accountName);
        this.balance = balance;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getAccountName() {
        return accountName;
    }

    public double getBalance() {
        return balance;
    }

    public abstract void withdraw(double amount);

    public void deposit(double amount) {
        balance += amount;
    }

}
