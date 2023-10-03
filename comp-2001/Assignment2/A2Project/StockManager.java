import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Manage the stock in a business.
 * The stock is described by zero or more Products.
 * 
 * @author Jager Cooper
 * @version 03/10/23
 */
public class StockManager
{
    // A list of the products.
    private ArrayList<Product> stock;

    /**
     * Initialise the stock manager.
     */
    public StockManager()
    {
        stock = new ArrayList<>();
    }

    /**
     * Add a product to the list.
     * @param item The item to be added.
     */
    public void addProduct(Product item)
    {
        stock.add(item);
    }
    
    /**
     * Receive a delivery of a particular product.
     * Increase the quantity of the product by the given amount.
     * @param id The ID of the product.
     * @param amount The amount to increase the quantity by.
     */
    public void delivery(int id, int amount)
    {
        Product p = findProduct(id);
        if (p != null)
        {
            p.increaseQuantity(amount);
        }
        else
        {
            System.out.println("No product with ID " + id);
        }
    }
    
    /**
     * Try to find a product in the stock with the given id.
     * @return The identified product, or null if there is none
     *         with a matching ID.
     */
    public Product findProduct(int id)
    {
        
        for (Product p : stock)
        {
            if (p.getID() == id)
            {
                return p;
            }
        }

        return null;
    }
    
    /**
     * Locate a product with the given ID, and return how
     * many of this item are in stock. If the ID does not
     * match any product, return zero.
     * @param id The ID of the product.
     * @return The quantity of the given product in stock.
     */
    public int numberInStock(int id)
    {
        Product product = this.findProduct(id);

        if (product != null){
            return product.getQuantity();
        }
        else {
            return 0;
        }
        
    }

    /**
     * Print details of all the products.
     */
    public void printProductDetails()
    {
        if (stock.size() == 0){
            System.out.println("There are no products in stock.");
        }
        else{
            for (Product p : stock)
            {
                System.out.println(p.toString());
            }
        }
    }

    /**
     * Print details of all the products with a stock level
     * below the given threshold. Implemented with Lambdas and Streams.
     * @param lowThreshold The threshold to use.
     */
    public void lowStock(int lowThreshold){
        if (stock.size() == 0) {
            System.out.println("There are no products in stock.");
        }

        else {
            // Streams, Filters, and collects to a list for validation
            List<Product> list = 
            stock.stream()
            .filter(products -> products.getQuantity() < lowThreshold)
            .collect(Collectors.toList());

            //Validates that the stream has at least one element that meets requirements
            if (list.size() == 0) {
                System.out.println("There are no products with a stock level below " + lowThreshold);
            } else {
                list.stream()
                .forEach(products -> System.out.println(products.toString()));
            }
            
        }
    }

    /**
     * Find a product with the given name.
     * @param name The name of the product.
     * @return The identified product, or null if there is none.
     */
    public Product findProduct(String name){
        for (Product p : stock)
        {
            if (p.getName().equals(name))
            {
                return p;
            }
        }
        
        return null;
    }
}
