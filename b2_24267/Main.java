package b2_24267;

import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int sum = 0, count = 0;
		long n = s.nextLong();
		
		System.out.printf("%d\n3",  n*(n-1)*(n-2)/6);
	}

}
/*
for(int i = 1; i <= n-2; i++) {
for(int j = i+1; j <= n-1; j++) {
	for(int k = j+1; k <=n; k++) {
		sum += i*j*k;
		count++;
	}
}
}
*/