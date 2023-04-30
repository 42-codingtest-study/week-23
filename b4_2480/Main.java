package b4_2480;
import java.util.Scanner;
	
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
		int sum = 0;
		if (a == b) {
			if (b == c) {
				sum = 10000+ 1000*a;
			}
			else
				sum = 1000+100*a;
		}
		else if (b == c) {
			sum = 1000+100*b;
		}
		else if (a == c) {
			sum = 1000+100*a;
		}
		else {
			int n;
			int N = (n = a>b?a:b)>c?n:c ; 
			sum = 100*N ;
		}
		System.out.print(sum);
	}

}
