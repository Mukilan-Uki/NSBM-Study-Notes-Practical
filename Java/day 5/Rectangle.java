class Book{
    String title = "Title";
    String author = "Author";
    int pages = 5;

    void displayDetails(){
        // method without return and parameters
        System.out.println("Title: "+title);
        System.out.println("Author: "+author);
        System.out.println("Pages: "+pages);

    }
}

class Rectangle{
    double length = 5;
    double width = 5;

    double calculateArea(){
        double area = length*width;

        System.out.println("Area: "+area);
    }
}
