class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result;
        for (int num : nums){
            result ^= num;
        }
        return result;
    }
};
