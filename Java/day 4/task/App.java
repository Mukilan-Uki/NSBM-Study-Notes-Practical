class App{
    public static void main(String[] args){
        Bill obj1 = new Bill();
        obj1.updateQuantity(5);
        obj1.displayOrder();
        obj1.calculateSubtotal();
        obj1.calculateFinalTotal(10);
    }
}