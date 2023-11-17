public class Cheque extends Account{
    private static final int minimBalance = 1000;
    private static final int overLimitCharge = 5;

    /**
     * Default Constructor
     */
    public Cheque(){
        super();
    }

    /**
     * Constructor with User name parameter
     * 
     * @param user String, user name to assign to the account
     */
    public Cheque(String user){
        super(user);
    }

    /**
     * Makes a withdraw from the account if the withdraw amount is less than the balance
     * of the account, and if the resulting balance is less than the minimBalance incurrs
     * the associated overLimitCharge
     * 
     * @param m Float, value to withdraw from the account
     */
    public void withdraw(float m){
        if (m <= balance) {
            if (balance - m < minimBalance){
                balance = balance - m - overLimitCharge;
            } else {
                balance = balance - m;
            }
        } else {
            System.out.println("Insufficient Funds");
        }
    }
    

}
