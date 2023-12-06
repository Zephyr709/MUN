public class Savings extends Account {

    private static final double WITHDRAW_FEE = 6.99;
    private static final double INTEREST = 0.019;

    public Savings(String accountName) {
        super(accountName);
    }

    public Savings(String accountName, double balance) {
        super(accountName, balance);
    }

}
