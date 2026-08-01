class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> answer(2 * nums.size());
        
        for (int i = 0; i < nums.size()*2; i++){
            answer[i] = nums[i%(nums.size())];
        }

        return answer;
    }
};