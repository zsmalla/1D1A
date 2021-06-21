package LEVEL1.java.NotFinishedPlayer;
import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);        // 배열 정렬 => java.util.Arrays api의 Arrays.sort()함수
        Arrays.sort(completion);
        for (int i = 0; i < completion.length; i++){
            if (!participant[i].equals(completion[i])) return participant[i];
//            if (!(participant[i] == completion[i])) return participant[i];        // ==은 객체의 주소(객체 자체)를 비교, equals()는 객체의 값을 비교
        }
        return participant[participant.length - 1];
    }
}

class otherSolution{
    /* 
    HashMap을 활용한 풀이
    HashMap은 Map 인터페이스를 구현한 대표적인 Map 컬렉션(Map 인터페이스를 상속) => 키와 값으로 구성된 Entry 객체를 저장하는 자료구조
    많은 양의 데이터를 검색하는데 있어서 뛰어난 성능
    */
    public String solution(String[] participant, String[] completion){
        String answer = " ";
        return answer;
    }
}