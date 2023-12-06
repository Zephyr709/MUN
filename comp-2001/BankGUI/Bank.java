import java.util.ArrayList;
import java.util.Iterator;

public class Bank {

    private String bankName;
    private String institutionNumber;
    private ArrayList<Account> accounts;

    public Bank() {
        bankName = "CIBC";
        institutionNumber = "150";
    }

    public Bank(String bankName, String institutionNumber) {
        this.bankName = bankName;
        this.institutionNumber = institutionNumber;
        accounts = new ArrayList<Account>();
    }

    public Bank(String bankName, String instutionNumber, String fileName) {
        this(bankName, instutionNumber);

    }

    public String getBankName() {
        return bankName;
    }

    public String getInstitutionNumber() {
        return institutionNumber;
    }

    public ArrayList<Account> getAccounts() {
        return accounts;
    }

    public void removeAccount(int accountNumber) {
        for (Iterator<Account> iterator = accounts.iterator(); iterator.hasNext();) {
            Account item = iterator.next();

            if (item.getAccountNumber() == (accountNumber)) {
                iterator.remove();
                return;
            }
        }
    }

}
