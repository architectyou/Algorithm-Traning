package JAVA_programming;

public class Main_4673 {

    public static void main(String[] args) {

        int[] numbers = new int[10000 + 1];

        for(int i = 1; i < numbers.length; i++) {
            int result_num = sequence_num(i);
            if (result_num < numbers.length) {
            numbers[result_num] += 1 ;
            }
        }

        for(int i = 1; i < numbers.length; i++){
            if (numbers[i] ==  0) {
                System.out.println(i);
            }
        }
    }

    public static int digit(int num) {
        if (num == 0) {
            return 0;
        } else {
            return num % 10 + digit(num / 10);
        }
    }

    public static int sequence_num(int num){
        int result = num + digit(num);
        return result;
    }
}
