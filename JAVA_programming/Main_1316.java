package JAVA_programming;

import java.util.Scanner;

public class Main_1316 {
    // 그룹단어 체커
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int cnt = 0;

        for(int i = 0 ; i < n ; i ++) {
            // next() -> 공백을 기준으로 한 단어 또는 한 문자씩 입력 받는다.
            // 버퍼에 입력된 문자나 문자열에서 공백 전까지의 단어를 읽는다. (개행 문자를 가져오지 않는다.)
            if (isGroupWord(input.next())) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }

    public static boolean isGroupWord(String word) {
        boolean[] checker = new boolean[26];
        int prev = 0;

        for (int i = 0 ; i < word.length() ; i++) {
            // String 타입의 문자열에서 특정 문자를 char 타입으로 변환
            int now = word.charAt(i);

            if (checker[now - 'a'] && now != prev) {
                return false;
            }

            checker[now - 'a'] = true;
            prev = now;
        }
        return true;
    }
}
