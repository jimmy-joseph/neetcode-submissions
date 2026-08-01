class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s1, s2;
        if (s.size() != t.size()){
            return false;
        }
        for (int i = 0; i < s.size(); i++){
            s1[s[i]] = s1[s[i]] + 1;
            s2[t[i]] = s2[t[i]] + 1;
        }
        for (const auto& entry : s1){
            if (s2[entry.first] != entry.second){
                return false;
            }
        }
        return true;
    }
};
