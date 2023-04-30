package b4_2439;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		
		for(int i = 0; i < n; i++) {
			
			for (int k = n - i; k > 1; k--)
				System.out.print(" ");
			for (int j = 0; j <= i; j++)
				System.out.print("*");
			
			System.out.print("\n");
		}
	}
}
