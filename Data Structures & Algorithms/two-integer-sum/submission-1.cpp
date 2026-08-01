class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> index_map;

        for (int i = 0; i < nums.size(); i++){
            int difference = target - nums[i];
            if (index_map.find(difference) != index_map.end()){
                return {index_map[difference], i};
            }
            index_map.insert({nums[i], i});
        }
    }
};
