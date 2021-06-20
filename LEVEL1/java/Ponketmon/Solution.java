package LEVEL1.java.Ponketmon;

import java.util.HashSet;           // java set interface

class Solution {
    public int solution(int[] nums) {
        int answer;
        int n = nums.length;        // array size check
        int N = n/2;                // 가져올 수 있는 폰켓몬 수
        HashSet<Integer> a = new HashSet<Integer>();
        for (int i = 0; i < n; i++){
            a.add(nums[i]);
        }

        if (a.size() < N) answer = a.size();
        else answer = N;
        
        return answer;
    }
}