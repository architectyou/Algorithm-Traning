package JAVA_programming;

import java.util.Scanner;

public class Main_10818 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();

        int minNum = Integer.MAX_VALUE;
        int maxNum = Integer.MIN_VALUE;

        for (int i = 0 ; i < n ; i ++ ){
            int num = input.nextInt();
            if (num < minNum) {
                minNum = num;
            }
            if (num > maxNum) {
                maxNum = num;
            }
        }
        System.out.println(minNum + " " + maxNum);

    }
}
