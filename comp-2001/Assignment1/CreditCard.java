import java.util.ArrayList;

public class CreditCard {
    String customerName;
    String accountNumber;
    float balance;
    float creditLimit;
    float creditAvail;
    ArrayList<Object> transactionHistory;
    

    public CreditCard(String name, String accountNum, float creditLim) {
        customerName = name;
        accountNumber = accountNum;
        balance = 0.00f;
        creditLimit = creditLim;
        creditAvail = 0.00f;
        transactionHistory = new ArrayList<>();

    }

    public String getCustomerName() {
        return customerName;
    }


    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    


}