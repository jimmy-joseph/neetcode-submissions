class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numCheck;
        int oldSize, newSize;
        for (int i = 0; i < nums.size(); i++){
            oldSize = numCheck.size();
            numCheck.insert(nums[i]);
            if (oldSize == numCheck.size()){
                return true;
            }
        }
        return false;
    }
};
