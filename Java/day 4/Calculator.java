class Calculator{
    // reference v
    int num1 = 20;
    int num2 = 10;

    // method 1
    // non parameterized | not return type = void method
    void addNumbers(){
        // method scope
        int tot = num1 + num2;
        System.out.println("Add: "+ tot);
    }

    // method 2
    // parameterized | non return type = void method
    void subNumbers(int a, int b){
        // method scope
        int sub = a - b;
        System.out.println("Sub: "+ sub);
    }

    // method 3
    // non parameterized | return type
    int divNumbers(){
        // method scope
        int divd = num1/num2;
        System.out.println("Div: "+ divd);
        return divd;
    }

    // method 4
    // parameterized | return type
    int multNumbers(int a, int b){
        // method scope
        int mult = a*b;
        System.out.println("Mult: "+mult);
        return mult;
    }
}