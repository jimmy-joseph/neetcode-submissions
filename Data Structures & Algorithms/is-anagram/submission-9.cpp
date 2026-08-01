class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charMap;

        if (t.size() != s.size()){
            return false;
        }
        for (int i = 0; i < s.size(); ++i){
            charMap[s[i]]++;
        }
        for (int i = 0; i < t.size(); ++i){
            if (--charMap[t[i]] < 0){
                return false;
            }
        }
        return true;
    }
};
