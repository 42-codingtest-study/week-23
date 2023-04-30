package b3_10818;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int arr[] = new int[s.nextInt()];
		for(int i = 0; i < arr.length; i++) {
			arr[i] = s.nextInt();
		}
		int max = arr[0], min = arr[0];
		for(int i = 1; i < arr.length; i++) {
			if(arr[i] > max) max = arr[i];
			if(arr[i] < min) min = arr[i];
		}
		System.out.printf("%d %d", min, max);

	}
}
/*
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		
		int n = s.nextInt();
		int first = s.nextInt();
		int max = first, min = first;
		for(int i = 1; i < n; i++) {
			int next = s.nextInt();
			if(next > max) max = next;
			if(next < min) min = next;
		}
		System.out.printf("%d %d", min, max);
	}

}
*/
