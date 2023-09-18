import java.util.ArrayList;

public class CreditCard {
    String customerName;
    String accountNumber;
    Float balance;
    Float creditLimit;
    Float creditAvail;
    ArrayList transactionHistory;
    

    public CreditCard(){

    }

    public String getCustomerName() {
        return customerName;
    }


    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    


}