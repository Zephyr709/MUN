public class Chequing extends Account {

    private static final double THRESHOLD = 1000;
    private static final double CHARGE = 6.99;

    public Chequing(String accountName) {
        super(accountName);

    }

    public Chequing(String accountName, double balance) {
        super(accountName, balance);
    }

    public void withdraw(double amount) {
        if (balance < THRESHOLD) {
            if ((amount + CHARGE) > balance) {
                System.out.println("You have insufficient funds to withdraw");
            } else {
                balance -= CHARGE + amount;
            }
        } else {
            balance -= amount;
        }
    }
}
