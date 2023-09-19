/*
 * Jager Cooper
 * 201765344
 */

import java.sql.Date;

public class Transaction {
    /* Class Attributes */
    private String source;
    private Date date; 
    /* new Date(); - Gets current Date 
     * Date.toString() -  Converts the date object to a string of 
     * the form: int(year,month,day,min,sec) 
     */
    private float amount;
    private String purchaseType;

    /* Constructor */
    public Transaction() {
        

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

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    
    public String toString() {
        return "a";
    }
}