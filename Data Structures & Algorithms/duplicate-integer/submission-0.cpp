class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> occurence_map;
        for (int n : nums) {
            if (occurence_map.contains(n)) return true;
            occurence_map.insert({n,1});
        }
        return false;
    }
};