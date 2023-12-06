import javax.swing.*;
import java.awt.*;

public class Gui {

    private Bank bank;
    private JFrame frame;
    private JPanel accountPanel;

    public Gui() {
        bank = new Bank();
        accountPanel = new JPanel();
        accountPanel.setLayout(new BoxLayout(accountPanel, BoxLayout.Y_AXIS));
        makeFrame();

    }

    private void makeFrame() {
        frame = new JFrame("Bank Manager");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(0, 1, 5, 5));

    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Bank Manager");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(0, 1, 5, 5));

    }
}
