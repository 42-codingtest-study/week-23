package s4_10610;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int[] bcd = new int[10];
		StringTokenizer st = new StringTokenizer(s.next());
		
		while(st.hasMoreTokens()) {
			++bcd[Integer.parseInt(st.nextToken())];
		}
	}

}
