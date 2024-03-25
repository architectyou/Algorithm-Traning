package JAVA_programming;

import java.util.Scanner;

public class Main_10872 {

    // 재귀함수 팩토리얼
    public static int factorial(int number) {
        if(number == 1){
            return 1;
        } else if (number == 0) {
            return 1;
        } else {
            return number * factorial(number-1);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        System.out.println(factorial(num));
    }
}