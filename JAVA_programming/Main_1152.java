package JAVA_programming;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Main_1152 {

    public static void main(String[] args) {
        //String Tokenizer를 이용하면 공백을 기준으로 나뉘어 토큰에 저장할 수 있음.
        //java.util.StringTokenizer;를 import 해 주어야 함

        Scanner input = new Scanner(System.in);
        String words = input.nextLine();

        StringTokenizer st = new StringTokenizer(words, " ");
        System.out.println(st.countTokens());
    }
}
    
