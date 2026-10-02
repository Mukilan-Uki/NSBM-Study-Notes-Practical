class App{
    
    public static void main(String[] args){
        Calculator obj1 = new Calculator();
        obj1.addNumbers();
        obj1.subNumbers(50, 8);
        obj1.divNumbers();
        obj1.multNumbers(4,3);

        Calculator obj2 = new Calculator();
        obj2.addNumbers();
        obj2.subNumbers(145,27);
        obj2.divNumbers();
        obj2.multNumbers(56,98);
    }
}