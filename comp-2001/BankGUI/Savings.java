public class Savings extends Account {

    private static final double WITHDRAW_FEE = 6.99;

    public Savings(String accountName) {
        super(accountName);
    }

    public Savings(String accountName, double balance) {
        super(accountName, balance);
    }

    public void withdraw(double amount) {
        if ((amount + WITHDRAW_FEE) > balance) {
            System.out.println("You have insufficent funds to withdraw");
        } else {
            balance -= WITHDRAW_FEE + amount;
        }
    }
}
