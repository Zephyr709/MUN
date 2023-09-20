/*
 * Jager Cooper
 * 201765344
 */

import java.time.LocalDateTime;

public class Transaction {
    /* Class Attributes */
    private String source;
    private LocalDateTime date; 
    /* new Date(); - Gets current Date 
     * Date.toString() -  Converts the date object to a string of 
     * the form: int(year,month,day,min,sec) 
     */
    private float amount;
    private String purchaseType;

    /* Constructor */
    public Transaction(String source, float amount, String purchaseType) {
        this.source = source;
        this.amount = amount;
        this.purchaseType = purchaseType;
        this.date = LocalDateTime.now();
        System.out.println(this.date);

    }
    
    /* Accessors and Mutators */
    public String getPurchaseType() {
        return purchaseType;
    }

    public void setPurchaseType(String purchaseType) {
        this.purchaseType = purchaseType;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public LocalDateTime getDate() {
        return date;
    }

    public void setDate(LocalDateTime date) {
        this.date = date;
    }

    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    
    public String toString() {
        return (
            "Source: " + source +
            "\nDate: " + date.toString() +
            "\nAmount: " + amount +
            "\nPurchase Type: " + purchaseType 
            );
    }
}