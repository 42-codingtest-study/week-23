package b4_11720;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int N = s.nextInt();
		//StringTokenizer st = new StringTokenizer(s.next());
		String str = s.next();
		String []tokens = str.split("");
		
		int sum = 0;
		/*
		for(int i = 0; i < st.countTokens(); i++) {
			sum += (Integer.parseInt(st.nextToken()));
		}
		*/
		for(int i = 0; i < str.length(); i++) {
			sum += Integer.parseInt(tokens[i]);
		}
		System.out.print(sum);
	}

}
