public class Saving extends Account {
    
    private static final float eachTimeCharge = 3.9f;

    /**
     * Default constructor
     */
    public Saving(){

    }
    /**
     * Constructor with user name parameter
     * 
     * @param user
     */
    public Saving(String user){

    }

    /**
     * Makes a withdraw from the account if the withdraw amount is less than or equal to the
     * the balance of the account and incurrs the associated eachTimeCharge 
     * 
     * @param m , Float value to withdraw from the account
     */
    public void withdraw(float m){
        if (m <= balance){
            balance = balance - m - eachTimeCharge;
        }
    }

    
}
