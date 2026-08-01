class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> numMap;
        for (int i = 0; i < nums.size(); ++i){
            if (numMap.contains(nums[i])){
                return true;
            }
            numMap.insert(nums[i]);
        }
        return false;
    }
};