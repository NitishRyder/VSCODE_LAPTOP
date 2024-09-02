import java.util.*;
public class SimpleSieve{
  public static void main(String args[]) {
  Scanner sc = new Scanner(System.in);
  System.out.print("Enter a number: ");
      int num = sc.nextInt();
      boolean[] bool = new boolean[num];
  for (int i = 0; i< bool.length; i++) {
         bool[i] = true;
      }
 for (int i = 2; i< Math.sqrt(num);i++){
         if(bool[i] == true) {
 for(int j = (i*i); j<num; j = j+i) {
               bool[j] = false;
         }
       }}          
System.out.print("List of prime numbers upto given number are : ");

int primeCount = 0;
int primeSum = 0;

for (int i = 2; i< bool.length; i++) {
         if(bool[i]==true) {
            System.out.print(i+" ");
            primeCount++;
            primeSum += i;
         }
      }
      System.out.println("Total prime: "+ primeCount);
      System.out.println("Sum of prime: "+ primeSum);
   }
}
