import java.util.Scanner;

public class AliceTree {
    static int minApples(int M,int K,int N,int S,int E,int W){
        if(M<=S*K){
            return M;
        }
        else if(M<=S*K+E+W){
            return S*K+(M-S*K);
        }
        else
        return -1;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the no.of apples to be collected: ");
        int M=sc.nextInt();

        System.out.println("Enter the no.of apples in each tree: ");
        int K=sc.nextInt();

        System.out.println("Enter the no.of trees in North: ");
        int N=sc.nextInt();

        System.out.println("Enter the no.of trees in South: ");
        int S=sc.nextInt();

        System.out.println("Enter the no.of trees in South: ");
        int W=sc.nextInt();

        System.out.println("Enter the no.of trees in South: ");
        int E=sc.nextInt();

        int ans = minApples(M, K, N, S, E, W);
        System.out.println(ans);
    }
}


