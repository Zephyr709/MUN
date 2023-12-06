
/**
 * The ATM class - An ATM interface.
 * @author (your name)
 * @version (a version number or a date)
 */
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ATM {
    private Bank bank;
    private String user;
    private JFrame frame;

    /**
     * Constructor for objects of class ATM
     */
    public ATM(String user) {
        this.user = user;
        createBankInfor();
        makeFrame();
    }

    private void createBankInfor() {
        // test example
        bank = new Bank("Canada");
        bank.add(new Saving(user));
        bank.add(new Saving(user));
        bank.add(new Cheque(user));
        bank.add(new Cheque(user));
    }

    /**
     * Create the frame
     */
    private void makeFrame() {
        frame = new JFrame("ATM");
        Container contentPane = frame.getContentPane();
        makeMenuBar(frame);
        listAccounts();
        frame.pack();
        frame.setVisible(true);
    }

    private void makeMenuBar(JFrame frame) {
        JMenuBar menubar = new JMenuBar();
        frame.setJMenuBar(menubar);

        JMenu menu;
        JMenuItem item;
        // create the Account menu
        menu = new JMenu("Accounts");
        menubar.add(menu);

        item = new JMenuItem("All Accounts...");
        item.addActionListener(e -> listAccounts());
        menu.add(item);
        // Q1. add a Checking menu item and its listener
        // your code goes here...
        JMenuItem chequing = new JMenuItem("Chequing accounts");
        chequing.addActionListener(e -> listAccounts("Cheque"));
        menu.add(chequing);

        // Q2. add a Saving menu item and its listener
        // your code goes here...

        JMenuItem saving = new JMenuItem("Saving Accounts");
        saving.addActionListener(e -> listAccounts("Saving"));
        menu.add(saving);

        // create the Help menu
        menu = new JMenu("Help");
        menubar.add(menu);
        item = new JMenuItem("About...");
        item.addActionListener(e -> about());
        menu.add(item);
        item = new JMenuItem("Exit...");
        menu.add(item);
        item.addActionListener(e -> System.exit(0));

    }

    private void listAccounts(String accType) {
        Container contentPane = frame.getContentPane();
        contentPane.removeAll();
        // Your may need to change this line (parameters of grid layout) to better
        // appearance after you finish coding
        contentPane.setLayout(new GridLayout(0, 6));
        for (Account acc : bank.getAccounts(user)) {
            if (!accType.equals(acc.getClass().getName())) {
                continue;
            }
            drawAccount(acc);
        }
        frame.pack();
        frame.setVisible(true);
    }

    private void listAccounts() {
        Container contentPane = frame.getContentPane();
        contentPane.removeAll();
        // Your may need to change this line (parameters of grid layout) to better
        // appearance after you finish coding
        contentPane.setLayout(new GridLayout(0, 6));
        for (Account acc : bank.getAccounts(user)) {
            drawAccount(acc);
        }
        frame.pack();
        frame.setVisible(true);
    }

    /*
     * Draw each account on the panel
     */
    private void drawAccount(Account acc) {
        Container contentPane = frame.getContentPane();
        JLabel label1 = new JLabel(acc.getClass().getName());
        contentPane.add(label1);

        // Q3. adding account number using a JLabel
        // your code goes here ...
        JLabel label2 = new JLabel("Account Number: " + acc.getAccountNo());
        contentPane.add(label2);

        JLabel label3 = new JLabel("Balance: ");
        contentPane.add(label3);
        // Add a JTestField field for displaying balance value
        JTextField tf1 = new JTextField(Float.toString(acc.getBalance()));
        contentPane.add(tf1);
        tf1.setEditable(false);

        // Add Deposit button and its listener
        JButton bDeposit = new JButton("Deposit");
        contentPane.add(bDeposit);
        // add event listener to the button, to pop up a dialog taking input
        bDeposit.addActionListener(
                ev -> {
                    String s = JOptionPane.showInputDialog("Input money: ", 0);
                    acc.deposit(s == null ? 0 : Float.parseFloat(s));
                    tf1.setText(Float.toString(acc.getBalance()));
                });

        // Q4. Add Withdraw button and its listener
        // your code goes here ...
        JButton bWithdraw = new JButton("Withdraw");
        contentPane.add(bWithdraw);
        bWithdraw.addActionListener(event -> {
            String s = JOptionPane.showInputDialog("Withdraw money: ", 0);
            if (s == null) {
                return;
            } else {
                acc.withdraw(Float.parseFloat(s));
                tf1.setText(Float.toString(acc.getBalance()));
            }
        });

    }

    private void about() {
        Container contentPane = frame.getContentPane();
        contentPane.removeAll();
        JLabel label1 = new JLabel(user + "@" + bank.getBankName());
        contentPane.add(label1);
        frame.pack();
        frame.setVisible(true);
    }
}
