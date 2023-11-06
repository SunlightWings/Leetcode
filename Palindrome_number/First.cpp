// This code didnt pass all the test cases, only 6538 / 11511 testcases passed
class Solution {
public:
    bool isPalindrome(int x) {
        float reversedNum = 0;
        int tmp = x;
        
        while (tmp > 0) {
            reversedNum = reversedNum * 10 + tmp % 10;
            tmp = tmp / 10;
        }
        
        return x == reversedNum;
    }
};
