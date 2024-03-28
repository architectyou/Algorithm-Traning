package Algorithm_Theory;

import java.util.Comparator;
import java.util.PriorityQueue;

// JAVA 에서는 Collection으로 Heap 이 제공되지 않는다. 하지만 Primary Queue를 활용하여 구현할 수 있다.

public class heap {
    
    // 최소 힙 사용하기 
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    // 최대 힙 사용하기 
    // 최대힙을 사용하기 위해서는 Comparator 값을 세팅해주어야 한다.
    PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(new Comparator<Integer>() {
      @Override
      public int compare(Integer o1, Integer o2){
        return - Integer.compare(o1, o2);
      }  
    });
    
}
