import java.util.ArrayList;

public class Bank {

    private String bankName;
    private String instutionNumber;
    private ArrayList<Account> accounts;

    public Bank(String bankName, String instutionNumber) {
        this.bankName = bankName;
        this.instutionNumber = instutionNumber;
        accounts = new ArrayList<Account>();
    }

    public Bank(String bankName, String instutionNumber, String fileName) {
        this(bankName, instutionNumber);

    }

    public String getBankName() {
        return bankName;
    }

    public String getInstutionNumber() {
        return instutionNumber;
    }

}
