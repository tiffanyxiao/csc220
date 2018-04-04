import java.util.Date;

public class Transaction implements Comparable<Transaction>{

    private String cardholder;
    private Date date;
    private Float amount;
    private String vendor;
    private String description;
    private String mcc;
//    private Boolean returnStatus;

    /**
     *
     * @param cardholder lastname and first initial
     * @param date YYYYMMDD formated date which allows for easiest comparison
     * @param amount amount as a float
     * @param vendor vendor name
     * @param description type of transaction
     * @param mcc merchant category code
     */
    Transaction(String cardholder, Date date, Float amount, String vendor, String description, String mcc){
        this.cardholder = cardholder;
        this.date = date;
        this.amount = amount;
        this.vendor = vendor;
        this.description = description;
        this.mcc = mcc.toLowerCase();

    }

    public Float getAmount(){
        return amount;
    }

    public String getCardholder(){
        return cardholder;
    }

    public String getMCC(){
        return mcc;
    }

    public Date getDate(){
        return date;
    }


    public String toString() {
        return  "NAME: " + cardholder + " DATE: " + date + " AMOUNT: " + amount  + " MCC: " + mcc ;

//        return   "amount: " + amount ;
    }

    @Override
    public int compareTo(Transaction other){
        return Float.compare(amount, other.amount);
    }
}