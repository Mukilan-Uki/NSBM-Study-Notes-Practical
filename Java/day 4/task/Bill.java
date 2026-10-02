class Bill{
    String customerName = "Mukilan";
    String foodItem = "Briyani";
    int unitPrice = 350;
    int quantity = 2;

    void displayOrder(){
        System.out.println("--- Order Details ---");
        System.out.println("\t");
        System.out.println("Customer Name: "+customerName);
        System.out.println("Food Item: "+foodItem);
        System.out.println("Unit Price: "+unitPrice);
        System.out.println("Quantity: "+quantity);
        System.out.println("\t");
    }

    void updateQuantity(int newQuantity){
        quantity = newQuantity;
        System.out.println("New Quantity: "+quantity);
        System.out.println("\t");
    }

    int calculateSubtotal(){
        int subtotal = unitPrice*quantity;
        System.out.println("Total Price: "+subtotal);
        System.out.println("\t");
        return subtotal;
    }

    int subtotal = calculateSubtotal();

    double calculateFinalTotal(double discountPercentage){
        double discount = subtotal*(discountPercentage/100);
        System.out.println(discount);
        System.out.println(subtotal);
        double finalBill = subtotal-discount;
        System.out.println("Your Final Bill: "+finalBill);
        return finalBill;
    }
}