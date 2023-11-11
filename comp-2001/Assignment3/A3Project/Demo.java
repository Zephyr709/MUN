import java.util.ArrayList;
import java.util.Random;

public class Demo {
    

    public static void main(String[] args){
        String user1 = "user1";
        String user2 = "user2";
        String user3 = "user3";
        String user4 = "user4";

        Saving saving1 = new Saving(user1);
        Saving saving2 = new Saving(user2);
        
        Cheque cheque1 = new Cheque(user3);
        Cheque cheque2 = new Cheque(user4);

        Saving saving3 = new Saving(user3);

        ArrayList<Account> accounts = new ArrayList<Account>();
        accounts.add(saving1);
        accounts.add(saving2);
        accounts.add(saving3);
        accounts.add(cheque1);
        accounts.add(cheque2);

        Random rand = new Random();

        for (Account account : accounts){
            float a = rand.nextFloat(500, 5000);
            float b = rand.nextFloat(500, 5000);

            System.out.println("Deposit: " + a );
            account.deposit(a);
            account.display();

            System.out.println("Withdraw: " + b );
            account.withdraw(b);
            account.display();


        }

        Bank bank = new Bank("CIBC");
        for (Account account : accounts){
            bank.add(account);
            
        }
        System.out.println("Displaying Bank Details:");
        bank.display();

        System.out.println("Displaying Bank Details with reference to a user:");
        bank.display(user3);
    }
}
