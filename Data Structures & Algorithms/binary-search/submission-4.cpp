class Solution {
public:
    int search(vector<int>& nums, int target) {
        int constraint = nums.size() - 1;
        int mid = 0;
        int start = 0;
        while (start <= constraint){
                mid = start + (constraint-start)/2;
                if (target < nums[mid]){
                    constraint = mid-1;
                } else if (target > nums[mid]){
                    start = mid+1;
                } else {
                    return mid;
                }
        }
        return -1;
    }
};
