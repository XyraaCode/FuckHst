public class FinalExampleTest {  
    //declaring final variable  
    final int age = 18;  
    void display() {  
      
    // reassigning value to age variable   
    // gives compile time error  
    age = 55;  
    }  
      
    public static void main(String[] args) {  
      
    FinalExampleTest obj = new FinalExampleTest();  
    // gives compile time error  
    obj.display();  
    }  
}
public class FinallyExample {    
      public static void main(String args[]){   
      try {    
        System.out.println("Inside try block");  
      // below code throws divide by zero exception  
       int data=25/0;    
       System.out.println(data);    
      }   
      // handles the Arithmetic Exception / Divide by zero exception  
      catch (ArithmeticException e){  
        System.out.println("Exception handled");  
        System.out.println(e);  
      }   
      // executes regardless of exception occurred or not   
      finally {  
        System.out.println("finally block is always executed");  
      }    
      System.out.println("rest of the code...");    
      }    
    }
public class FinalizeExample {    
     public static void main(String[] args)     
    {     
        FinalizeExample obj = new FinalizeExample();        
        // printing the hashcode   
        System.out.println("Hashcode is: " + obj.hashCode());           
        obj = null;    
        // calling the garbage collector using gc()   
        System.gc();     
        System.out.println("End of the garbage collection");     
    }     
   // defining the finalize method   
    protected void finalize()     
    {     
        System.out.println("Called the finalize() method");     
    }     
}
public class TestThrow {  
    //defining a method  
    public static void checkNum(int num) {  
        if (num < 1) {  
            throw new ArithmeticException("\nNumber is negative, cannot calculate square");  
        }  
        else {  
            System.out.println("Square of " + num + " is " + (num*num));  
        }  
    }  
    //main method  
    public static void main(String[] args) {  
            TestThrow obj = new TestThrow();  
            obj.checkNum(-3);  
            System.out.println("Rest of the code..");  
    }  
}
public class TestThrows {  
    //defining a method  
    public static int divideNum(int m, int n) throws ArithmeticException {  
        int div = m / n;  
        return div;  
    }  
    //main method  
    public static void main(String[] args) {  
        TestThrows obj = new TestThrows();  
        try {  
            System.out.println(obj.divideNum(45, 0));  
        }  
        catch (ArithmeticException e){  
            System.out.println("\nNumber cannot be divided by 0");  
        }  
          
        System.out.println("Rest of the code..");  
    }  
}
