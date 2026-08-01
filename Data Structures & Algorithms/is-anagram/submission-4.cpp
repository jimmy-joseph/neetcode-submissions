class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charMap;

        for (int i = 0; i < s.size(); ++i){
            if (charMap.contains(s[i])){
                charMap[s[i]] = charMap[s[i]] + 1;
            } else {
                charMap[s[i]] = 1;
            }
        }
        for (int i = 0; i < t.size(); ++i){
            if (charMap.contains(t[i])){
                charMap[t[i]] = charMap[t[i]] - 1;
                if (charMap[t[i]] == 0){
                    charMap.erase(t[i]);
                }
            } else {
                return false;
            }
        }
        if (charMap.size() == 0){
            return true;
        }
        return false;
    }
};
