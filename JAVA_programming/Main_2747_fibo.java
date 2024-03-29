package JAVA_programming;

import java.util.Scanner;

public class Main_2747_fibo {
    
    // 재귀적 피보나치 함수는 간단하고 이해가 쉽지만, 컴퓨터가 실제로 실행할 때는 많은 계산이 중복되어 매우 비효율적이다.
    // 문제 해결 방법
        // 동적 계획 법 -> 저장된 값을 이용하는 방법 
        // 피보나치 수를 한 번만 계산하고, 이를 배열에 저장하여 재사용함으로써 중복 게산을 피한다. (Memoization) 이라고 한다.
        
        // 반복적 방법
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();

        // dp 저장값 만들기
        int[] fiboCache = new int[num+1];
        System.out.println(fibo(num, fiboCache));
    }

    public static int fibo (int num, int[] cache) {
        if (num == 0) {
            return 0;
        }
        if (num == 1 | num == 2) {
            return 1;
        }
        if (cache[num] != 0) {
            return cache[num];
        }
        cache[num] = fibo(num-1, cache) + fibo(num-2, cache);
        return cache[num];
    }
}
